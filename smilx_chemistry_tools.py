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
#-------------------------------------------------------------------------------------------------