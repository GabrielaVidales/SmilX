import re
import copy
#-----------------------------------------------------------------------------------Unsaturation degrees
def delete_unsaturation_invalid(list_unsaturations):
    i_pos = 0
    reg_unsaturations = set()
    while i_pos < len(list_unsaturations):
      code_unsaturations = (list_unsaturations[i_pos].single_bonds,
                            list_unsaturations[i_pos].double_bonds,
                            list_unsaturations[i_pos].triple_bonds,
                            list_unsaturations[i_pos].cycles)
      if code_unsaturations in reg_unsaturations or not(list_unsaturations[i_pos].is_valid_unsaturation):
        del list_unsaturations[i_pos]
      else:
        reg_unsaturations.add(code_unsaturations)
        i_pos += 1
    return list_unsaturations

def get_unsaturations(molecular_formula, n_heavy_atoms):
  initial_list = [unsaturation(molecular_formula, n_heavy_atoms)]
  final_list = []
    
  if molecular_formula["hdi"] % 2 == 0:
    limit_unsaturations = 0
  else:
    limit_unsaturations = 1
      
  while initial_list[-1].double_bonds > limit_unsaturations:
    initial_list.append(initial_list[-1].clonate())
    initial_list[-1].triple_bonds += 1
    initial_list[-1].double_bonds -= 2
    initial_list[-1].update_single_bonds(n_heavy_atoms)
    initial_list[-1].update_validity()

  for i_unsaturation in initial_list:
    new_unsaturation = i_unsaturation.clonate()
    while new_unsaturation.double_bonds > 0:
      new_unsaturation.double_bonds -= 1
      new_unsaturation.cycles += 1
      new_unsaturation.update_single_bonds(n_heavy_atoms)
      new_unsaturation.update_validity()
      final_list.append(copy.deepcopy(new_unsaturation))

  final_list = delete_unsaturation_invalid(initial_list + final_list)
  final_list.sort(key=lambda x: (x.cycles, x.double_bonds + x.triple_bonds))

  return final_list

class unsaturation:
  def __init__(self, molecular_formula, n_heavy_atoms):
    self.double_bonds = molecular_formula["hdi"]
    self.triple_bonds = 0
    self.cycles = 0
    self.update_single_bonds(n_heavy_atoms)
    self.update_validity()

  def clonate(self):
    return copy.deepcopy(self)

  def update_single_bonds(self, n_heavy_atoms):
    self.single_bonds = n_heavy_atoms - 1 - self.double_bonds - self.triple_bonds

  def update_validity(self):
    if self.single_bonds < 0:
      self.is_valid_unsaturation = False
    else:
      self.is_valid_unsaturation = True

  def show_unsaturations(self):
    return f'Single bonds:{self.single_bonds}, Double bonds:{self.double_bonds}, Triple bonds:{self.triple_bonds}, Cycles:{self.cycles}'

#-----------------------------------------------------------------------------------Molecular formula
def get_hdi(molecular_formula):
    hdi = 2
    dict_valences={'C':4,
                   'N':3, 'P':3, 'B':3,
                   'S':2, 'O':2,
                   'H':1, 'F':1, 'I':1, 'Cl':1, 'Br':1}
    for i_element in molecular_formula:
        hdi += molecular_formula[i_element]*(dict_valences[i_element] - 2)
    if hdi % 2 == 0 and hdi > -1:
        return int(0.5*hdi)
    else:
        return None
#-----------------------------------------------------------------------------------Class standard_smiles
class standard_smiles:
    def __init__(self, n_heavy_atoms):
        self.molecular_formula = None
        self.target_n_heavy_atoms = n_heavy_atoms
        self.current_heavy_atom_count = 0
        self.standard_smiles = []
        self.smiles = None
        self.hdi = 0
        self.branches = []
        self.bonds = dict()
        self.bonds_cycles = set()
        self.list_cycles = []
        self.atoms = ['C' for i_atom in range(self.target_n_heavy_atoms)]
        self.grades = []
        self.adjacency_list = dict()
        self.nesting_levels = []
        self.level = 0
        self.pile = 0
        self.pivot = -1
        self.terminal_nodes = 0

#---------------------------------------------------------------------------------Methods alkanes
    def get_path(self, start, end):
        # Verificar si los nodos existen en el grafo
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return -1, []  # Indica que los nodos no existen o no hay camino
    
        # Cola para la búsqueda en amplitud (nodo, distancia, camino recorrido)
        queue = [(start, 0, [start])]
        # Conjunto para rastrear los nodos visitados
        visited = set()
    
        while queue:
            current_node, distance, path = queue.pop(0)
    
            # Si encontramos el nodo objetivo, devolvemos la distancia y el camino
            if current_node == end:
                return path
    
            # Marcar el nodo como visitado
            visited.add(current_node)
    
            # Agregar los nodos vecinos no visitados a la cola
            for neighbor in self.adjacency_list[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1, path + [neighbor]))
    
        # Si no encontramos el nodo objetivo, devolvemos -1 y una lista vacía
        return []

    def get_terminal_nodes(self):
        self.terminal_nodes = 0
        for i_neighbors in self.adjacency_list.values():
            if len(i_neighbors) == 1:
              self.terminal_nodes += 1

    def clonate(self):
        return copy.deepcopy(self)
    
    def update_smiles(self):
        self.smiles = ''.join(self.standard_smiles)
    
    def update_grade(self):
        if self.current_heavy_atom_count == 1:
          self.grades.append(0)
        else:
          self.grades.append(1)
          self.grades[self.pivot] += 1

    def update_pile(self):
        dict_brach={0 : 0,
                    1 : 0,
                    2 : 1,
                    3 : -1}
        self.pile += dict_brach[self.branches[-1]]

    def update_nesting_levels(self):
        if self.branches[-1] == 0:
            self.nesting_levels.append(self.level)
        elif self.branches[-1] == 1:
            self.level+=1
            self.nesting_levels.append(self.level)
            self.level-=1
        elif self.branches[-1] == 2:
            self.level+=1
            self.nesting_levels.append(self.level)
        else:
            self.nesting_levels.append(self.level)
            self.level-=1

    def update_list_adyacency(self):
        if self.current_heavy_atom_count == 1:
          self.adjacency_list[0] = set()
        else:
          self.adjacency_list[self.pivot].add(self.current_heavy_atom_count - 1)
          self.adjacency_list[self.current_heavy_atom_count - 1] = {self.pivot}
    
          bond = (self.pivot, self.current_heavy_atom_count - 1)
          self.bonds[bond] = 1

    def update_pivot(self):
        if self.current_heavy_atom_count == 1:
          self.pivot = 0
        else:
          branch = (self.branches[-2], self.branches[-1])
          if branch in {(0,0), (0,2), (1,0), (2,0), (1,2), (2,2), (3,0), (3,2)}:
            self.pivot = self.current_heavy_atom_count - 1
    
          elif branch in {(0,1), (2,1)}:
            self.pivot = self.current_heavy_atom_count - 2
    
          elif branch == (1,1):
            self.pivot = self.current_heavy_atom_count - 3
    
          elif branch in {(0,3), (1,3), (2,3), (3,3), (3,1)}:
            for i_pos in range(-2, - self.current_heavy_atom_count - 1, -1):
    
              if (self.branches[i_pos] in {0, 2} and
                  self.nesting_levels[i_pos] + 1 == self.nesting_levels[-1]):
    
                self.pivot = self.current_heavy_atom_count + i_pos
                break

    def add_carbon_atom(self, syntax_rule):
        if self.current_heavy_atom_count < self.target_n_heavy_atoms:
            dict_syntax_rule = {0 : "C",
                                1 : "(C)",
                                2 : "(C",
                                3 : "C)"}
            self.current_heavy_atom_count += 1
            self.branches.append(syntax_rule)
            self.update_nesting_levels()
            self.update_grade()
            self.update_list_adyacency()
            self.update_pivot()
            self.update_pile()
            self.standard_smiles.append(dict_syntax_rule[syntax_rule])
            self.update_smiles()
            self.get_terminal_nodes()

    def if_satisfy_constraint_0_and_1(self):
        if self.target_n_heavy_atoms - self.current_heavy_atom_count > 2:
          return self.target_n_heavy_atoms - self.current_heavy_atom_count - 2 > self.pile
        else:
          return True
    
    def if_satisfy_constraint_2(self):
        return self.pile <= self.pile + 1 <= self.target_n_heavy_atoms - self.current_heavy_atom_count - 2 - 1

    def replicate(self, syntax_rules):
        if self.current_heavy_atom_count == self.target_n_heavy_atoms:
          return new_smiles[self]
        else:
          new_smiles = []
          for i_rule in syntax_rules:
    
            if i_rule == 0 and self.if_satisfy_constraint_0_and_1():
    
              new_instance=self.clonate()
              new_instance.add_carbon_atom(i_rule)
              new_smiles.append(copy.deepcopy(new_instance))
    
            elif (i_rule == 1 and
                  self.grades[self.pivot] < 3 and
                  self.branches[-1] != 3 and
                  self.if_satisfy_constraint_0_and_1()):
    
              new_instance=self.clonate()
              new_instance.add_carbon_atom(i_rule)
              new_smiles.append(copy.deepcopy(new_instance))
    
            elif (i_rule == 2 and 
                  self.grades[self.pivot] < 3 and 
                  self.if_satisfy_constraint_2()):
    
              new_instance=self.clonate()
              new_instance.add_carbon_atom(i_rule)
              new_smiles.append(copy.deepcopy(new_instance))
    
            elif i_rule == 3 and self.pile > 0:
    
              new_instance=self.clonate()
              new_instance.add_carbon_atom(i_rule)
              new_smiles.append(copy.deepcopy(new_instance))
    
          return new_smiles

  #-----------------------------------------------------------------------------------------
    def is_valid_add_double_bond(self, bond):
        if bond in self.bonds:
            if (self.bonds[bond] == 1 and 
                4 - self.grades[bond[0]] > 0 and 
                4 - self.grades[bond[1]] > 0):
                return True
            else:
                return False
        else:
            return False
    
    def add_double_bond(self, bond):
        self.standard_smiles[bond[1]] = self.standard_smiles[bond[1]].replace('C','=C')
        self.bonds[bond] = 2
        self.hdi += 1
        self.grades[bond[0]] += 1
        self.grades[bond[1]] += 1
        self.update_smiles()

    def replicate_simple_dehydrogenation(self):
        smiles_dehydrogenated = []
        for i_bond in self.bonds.keys():
          if self.is_valid_add_double_bond(i_bond):
            new_instance = self.clonate()
            new_instance.add_double_bond(i_bond)
            smiles_dehydrogenated.append(copy.deepcopy(new_instance))
        return smiles_dehydrogenated
    
    #-------------------------------------------------------------------------------------------------
    def is_valid_add_triple_bond(self, bond):
        if bond in self.bonds:
            if (self.bonds[bond] == 1 and 
                4 - self.grades[bond[0]] > 1 and 
                4 - self.grades[bond[1]] > 1):
                return True
            else:
                return False
        else:
          return False

    def add_triple_bond(self, bond):
        self.standard_smiles[bond[1]] = self.standard_smiles[bond[1]].replace('C','#C')
        self.bonds[bond] = 3
        self.hdi += 2
        self.grades[bond[0]] += 2
        self.grades[bond[1]] += 2
        self.update_smiles()
    
    def replicate_double_dehydrogenation(self):
        smiles_dehydrogenated = []
        for i_bond in self.bonds.keys():
          if self.is_valid_add_triple_bond(i_bond):
            new_instance = self.clonate()
            new_instance.add_triple_bond(i_bond)
            smiles_dehydrogenated.append(copy.deepcopy(new_instance))
        return smiles_dehydrogenated

#-------------------------------------------------------------------------------------------------
    def is_valid_add_cycle(self, cycle):
        set_cycle = set(self.get_path(cycle[0], cycle[1]))
        if (self.grades[cycle[0]] < 4 and
            self.grades[cycle[1]] < 4 and
            cycle[1] not in self.adjacency_list[cycle[0]] and
            cycle not in self.bonds_cycles):
            for i_cycle in self.list_cycles:
                if set_cycle.issubset(i_cycle):
                    return False
            else:
                return True
        else:
          return False
    
    def get_possible_cycles(self):
        possible_cycles = []
        for i_atom in range(self.target_n_heavy_atoms - 1):
          for j_atom in range(i_atom + 1, self.target_n_heavy_atoms):
            if self.is_valid_add_cycle((i_atom, j_atom)):
              possible_cycles.append((i_atom, j_atom))
        return possible_cycles

    def add_cycle(self, cycle):
        count_cycles = len(self.bonds_cycles)
        if count_cycles < 9:
          self.standard_smiles[cycle[0]] = self.standard_smiles[cycle[0]].replace('C',f'C{count_cycles + 1}')
          self.standard_smiles[cycle[1]] = self.standard_smiles[cycle[1]].replace('C',f'C{count_cycles + 1}')
        elif count_cycles > 8:
          self.standard_smiles[cycle[0]] = self.standard_smiles[cycle[0]].replace('C',f'C%{count_cycles + 1}')
          self.standard_smiles[cycle[1]] = self.standard_smiles[cycle[1]].replace('C',f'C%{count_cycles + 1}')
        self.update_smiles()
        self.bonds_cycles.add(cycle)
        self.list_cycles.append(set(self.get_path(cycle[0], cycle[1])))
        self.adjacency_list[cycle[0]].add(cycle[1])
        self.adjacency_list[cycle[1]].add(cycle[0])
        self.hdi += 1
        self.grades[cycle[0]] += 1
        self.grades[cycle[1]] += 1
    
    def replicate_cycling(self):
        smiles_cycled = []
        possible_cycles = self.get_possible_cycles()
        for i_cycle in possible_cycles:
            if self.is_valid_add_cycle(i_cycle):
              new_instance = self.clonate()
              new_instance.add_cycle(i_cycle)
              smiles_cycled.append(copy.deepcopy(new_instance))
        return smiles_cycled

#-------------------------------------------------------------------------------------------------
    def replace_atom(self, atom, position):
        if atom not in {"C", "H", "hdi"}:
            self.standard_smiles[position] = self.standard_smiles[position].replace('C', atom)
            self.update_smiles()
            self.atoms[position] = atom
            self.molecular_formula[atom] -= 1
    
    def replicate_replacing_atoms(self):
        valences={"N":3,
                  "P":3,
                  "B":3,
                  "S":2,
                  "O":2,
                  "F":1, "I":1, "Cl":1, "Br":1}
        smiles_replaced = []
        for i_element, i_atoms in self.molecular_formula.items():
          if i_element not in {"C", "H", "hdi"} and i_atoms > 0:
              for i_pos in range(self.target_n_heavy_atoms):
                if self.atoms[i_pos] == "C" and self.grades[i_pos] <= valences[i_element]:
                  new_instance = self.clonate()
                  new_instance.replace_atom(i_element, i_pos)
                  smiles_replaced.append(copy.deepcopy(new_instance))
        return smiles_replaced
#-----------------------------------------------------------------------------------class SmilesCarbened
class smiles_carbened:
    def __init__(self, string_smiles):
        self.smiles = copy.deepcopy(string_smiles)

        self.get_type_smiles()
        self.get_atoms_from_smiles()
        self.get_connectivity()
        self.get_list_adjacency()
        self.get_list_hydrogens()
        self.get_list_degrees()

        self.molecular_formula = {}
        self.rings = 0

        self.charges = [0 for _ in range(len(self.atoms))]
        self.charge = 0

        self.index_cycles = []


    # Get the SMILES type
    def get_type_smiles(self):
        self.class_smiles = ""

        if "(" in "".join(self.smiles):
            self.type_smiles = "Branched"
        else:
            self.type_smiles = "Linear"

    # Get a list of atoms from SMILES
    def get_atoms_from_smiles(self):
        self.atoms = []

        atom_patterns = [
            'Cl', 'Br', 'Si', '[C]', '[CH]', 'C', 'N', 'O', 'S',
            'P', 'B', 'F', 'I'
        ]

        for iword in self.smiles:
            for atom in atom_patterns:
                if atom in iword:
                    if atom in ['[C]', '[CH]']:
                        self.atoms.append('[C]')
                    else:
                        self.atoms.append(atom)
                    break

    def get_connectivity(self):
        self.bonds = {}

        def rank_level_smiles():
            list_levels = []
            level = 0

            for i_word in self.smiles:
                if "(" not in i_word and ")" not in i_word:
                    list_levels.append(level)
                else:
                    if "(" in i_word and ")" not in i_word:
                        level += 1
                        list_levels.append(level)
                    elif "(" in i_word and ")" in i_word:
                        level += 1
                        list_levels.append(level)
                        level -= 1
                    elif "(" not in i_word and ")" in i_word:
                        list_levels.append(level)
                        level -= 1

            return list_levels

        # -----------------------------------------------------------------------
        # Get linear connectivity
        rank_levels = rank_level_smiles()
        level = 0

        for i_level in range(len(rank_levels)):
            if ")" in self.smiles[i_level]:
                level -= 1
                continue

            level = rank_levels[i_level]

            for j_level in range(i_level + 1, len(rank_levels)):
                if rank_levels[j_level] == rank_levels[i_level]:
                    if "=" in self.smiles[j_level]:
                        self.bonds[(i_level, j_level)] = "="
                    elif "#" in self.smiles[j_level]:
                        self.bonds[(i_level, j_level)] = "#"
                    else:
                        self.bonds[(i_level, j_level)] = ""
                    break
                else:
                    if level == rank_levels[i_level] and "(" in self.smiles[j_level]:
                        level += 1

                        if "=" in self.smiles[j_level]:
                            self.bonds[(i_level, j_level)] = "="
                        elif "#" in self.smiles[j_level]:
                            self.bonds[(i_level, j_level)] = "#"
                        else:
                            self.bonds[(i_level, j_level)] = ""

                        if ")" in self.smiles[j_level]:
                            level -= 1
                    else:
                        if level != rank_levels[i_level] and "(" in self.smiles[j_level]:
                            level += 1
                        if level != rank_levels[i_level] and ")" in self.smiles[j_level]:
                            level -= 1

        # -----------------------------------------------------------------------
        # Get non-linear connectivity
        list_nonlinear_connectivity = []

        for i_word in self.smiles:
            flag = 0
            connectors = []

            for i_symbol in i_word:
                if i_symbol.isdigit() and flag == 0:
                    connectors.append(i_symbol)
                elif i_symbol == "%" and flag == 0:
                    percent = "%"
                    flag = 2
                elif flag == 2 or flag == 1:
                    percent += i_symbol
                    if flag == 1:
                        connectors.append(percent)
                    flag -= 1

            list_nonlinear_connectivity.append(connectors)

        for i_index in range(len(list_nonlinear_connectivity) - 1):
            for i_connector in list_nonlinear_connectivity[i_index]:
                for j_index in range(i_index + 1, len(list_nonlinear_connectivity)):
                    if i_connector in list_nonlinear_connectivity[j_index]:
                        self.bonds[(i_index, j_index)] = ""
                        list_nonlinear_connectivity[j_index].remove(i_connector)
                        break

    def get_list_adjacency(self):
        self.adjacency = []

        list_nodes = list(
            set([i_bond[0] for i_bond in self.bonds] + [j_bond[1] for j_bond in self.bonds])
        )

        list_adjacency = [[] for _ in range(len(list_nodes))]
        self.adjacency = dict(zip(list_nodes, list_adjacency))

        for i_bond in self.bonds:
            self.adjacency[i_bond[0]].append(i_bond[1])
            self.adjacency[i_bond[1]].append(i_bond[0])


def get_list_hydrogens(self):
    self.hydrogens = []

    list_bonds = [0 for _ in range(len(self.atoms))]
    dic_bonds = {"": 1, "=": 2, "#": 3}

    for i_bond in self.bonds:
        bond_order = dic_bonds[self.bonds[i_bond]]
        list_bonds[i_bond[0]] += bond_order
        list_bonds[i_bond[1]] += bond_order

    for i_pos in range(len(self.atoms)):
        atom = self.atoms[i_pos]
        bonds = list_bonds[i_pos]

        if atom == "C":
            if bonds > 4:
                self.hydrogens.append(0)
            else:
                self.hydrogens.append(4 - bonds)

        elif atom == "S":
            if bonds in {2, 4, 6}:
                self.hydrogens.append(0)
            elif bonds in {1, 3, 5}:
                self.hydrogens.append(1)

        elif atom == "P":
            if bonds in {3, 5, 6}:
                self.hydrogens.append(0)
            elif bonds in {2, 4}:
                self.hydrogens.append(1)
            elif bonds == 1:
                self.hydrogens.append(2)

        elif atom == "N":
            if bonds in {3, 4, 5, 6}:
                self.hydrogens.append(0)
            elif bonds == 2:
                self.hydrogens.append(1)
            elif bonds == 1:
                self.hydrogens.append(2)

        elif atom in {"O", "[C]"}:
            if bonds in {2, 3, 4, 5, 6}:
                self.hydrogens.append(0)
            elif bonds == 1:
                self.hydrogens.append(1)

        elif atom in {"Cl", "Br", "I", "F"}:
            self.hydrogens.append(0)

    def get_list_degrees(self):
        self.degrees = [0 for _ in range(len(self.smiles))]

        bond_weights = {"": 1, "=": 2, "#": 3}

        for i_bond in self.bonds:
            weight = bond_weights[self.bonds[i_bond]]
            self.degrees[i_bond[0]] += weight
            self.degrees[i_bond[1]] += weight


    def update_list_hydrogen_atoms(self):
        self.molecular_formula['H'] = sum(self.hydrogens)

#------------------------------------------------------------------------------------------------------------Transformation chemical methods
    def dehydrogenate(self, bond):
        if (
            self.hydrogens[bond[0]] > 0
            and self.hydrogens[bond[1]] > 0
            and self.molecular_formula['hdi'] > 0
        ):
            if self.bonds[bond] == '':
                self.bonds[bond] = '='
                self.smiles[bond[1]] = self.smiles[bond[1]].replace('C', '=C')

            elif self.bonds[bond] == '=':
                self.bonds[bond] = '#'
                self.smiles[bond[1]] = self.smiles[bond[1]].replace('=C', '#C')

            self.molecular_formula['hdi'] -= 1
            self.hydrogens[bond[0]] -= 1
            self.hydrogens[bond[1]] -= 1
            self.degrees[bond[0]] += 1
            self.degrees[bond[1]] += 1

    def cycle(self, atoms, type_ring):
        if (
            self.hydrogens[atoms[0]] >= type_ring
            and self.hydrogens[atoms[1]] >= type_ring
            and self.molecular_formula["hdi"] > 0
            and atoms not in self.bonds
        ):
            symbol_ring = {1: "", 2: "=", 3: "#"}
            ring = self.rings + 1

            self.rings += 1
            self.adyacency[atoms[0]].append(atoms[1])
            self.adyacency[atoms[1]].append(atoms[0])

            self.bonds[atoms] = symbol_ring[type_ring]

            self.hydrogens[atoms[0]] -= type_ring
            self.hydrogens[atoms[1]] -= type_ring

            self.degrees[atoms[0]] += 1
            self.degrees[atoms[1]] += 1

            self.molecular_formula["hdi"] -= type_ring

            if ring < 10:
                self.smiles[atoms[0]] = self.smiles[atoms[0]].replace(
                    "C", f"C{ring}"
                )
                self.smiles[atoms[1]] = self.smiles[atoms[1]].replace(
                    "C", f"C{symbol_ring[type_ring]}{ring}"
                )
            else:
                self.smiles[atoms[0]] = self.smiles[atoms[0]].replace(
                    "C", f"C%{ring}"
                )
                self.smiles[atoms[1]] = self.smiles[atoms[1]].replace(
                    "C", f"C{symbol_ring[type_ring]}%{ring}"
                )

    def substitution_carbon_dehydrogenation(self, atom, position):
        valences = {
            "C": 4, "Si": 4, "O": 2, "S": 2, "[C]": 2,
            "N": 3, "P": 3, "B": 3,
            "Cl": 1, "Br": 1, "I": 1, "F": 1
        }

        if atom != "C" and self.degrees[position] <= valences[atom]:
            self.molecular_formula[atom] -= 1
            self.hydrogens[position] = valences[atom] - self.degrees[position]
            self.atoms[position] = atom

            self.smiles[position] = self.smiles[position].replace("C", atom)

            if atom == "[C]" and self.hydrogens[position] == 1:
                self.smiles[position] = self.smiles[position].replace("C", "CH")
        else:
            self.molecular_formula[atom] -= 1

        self.update_list_hydrogen_atoms()
#----------------------------------------------------------------------------------------------------------------------------------------
"""
    def Get_Atom_Hybridization(self):
        VALUE_PI_BOND={'':0,'=':1,'#':2}
        VALUE_HIBRIDATION={4:'sp3',3:'sp2',2:'sp'}
        LIST_STERIC_NUMBER=np.array([0 for i in range(len(self.ATOMS))])
        # CONSTUIR UNA LISTA PARA LOS ENLACES PI
        LIST_PI_BOND=[0 for i in range(len(self.ATOMS))]
        for iBOND in self.BONDS:
            LIST_PI_BOND[iBOND[0]]+=VALUE_PI_BOND[self.BONDS[iBOND]]
            LIST_PI_BOND[iBOND[1]]+=VALUE_PI_BOND[self.BONDS[iBOND]]
        #------------------------------------------------------------------------------Add SIGMA BONDS
        # AÑADIR LA CANTIDA DE ENLACES SIGMA DEL TIPO A-A
            LIST_STERIC_NUMBER[iBOND[0]]+=1
            LIST_STERIC_NUMBER[iBOND[1]]+=1
        # AÑADIR LA CANTIDA DE ENLACES SIGMA DEL TIPO A-H
        LIST_STERIC_NUMBER+=np.array(self.HYDROGENS)
        #-----------------------------------------------------------------------------Add lone electrons
        # AÑADIR LA CANTIDA DE PARES DE ELECTRONES LIBRES
        for iPOS in range(len(self.ATOMS)):
            if self.ATOMS[iPOS]!='C':
                LIST_STERIC_NUMBER[iPOS]+=int((8-2*(LIST_STERIC_NUMBER[iPOS]+LIST_PI_BOND[iPOS]))/2)
        #-----------------------------------------------------------------------------Establish Hybridizations
        # ESTABLECER HIBRIDACIONES PARA CADA ÁTOMO
        self.HIBRIDATIONS=[]
        for iNUMBER in LIST_STERIC_NUMBER:
            if iNUMBER>1:
                self.HIBRIDATIONS.append(VALUE_HIBRIDATION[iNUMBER])
            else:
                self.HIBRIDATIONS.append(False)"""
