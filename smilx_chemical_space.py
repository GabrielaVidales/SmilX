import os
import numpy as np
import shutil
import pickle
import copy
from tqdm import tqdm
from smilx_chemistry_tools import standard_smiles
from smilx_chemistry_tools import smiles_carbened
from rdkit import Chem
from rdkit.Chem import AllChem
import streamlit as st
import pandas as pd
import mols2grid

def list_files(path_folder):
    """
    Lista los archivos con extensión .pkl en la carpeta especificada.

    :param carpeta: Ruta de la carpeta donde buscar los archivos .pkl
    :return: Lista de nombres de archivos con extensión .pkl
    """
    try:
        files_pkl = []
        for file in os.listdir(path_folder):
            if file.endswith('.pkl'):
                name, extension = os.path.splitext(file)
                files_pkl.append(name)
        return files_pkl
    except FileNotFoundError:
        print(f"Error: La carpeta '{path_folder}' no existe.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def check_folder_src(path_folder):
    """
    Verifica si una carpeta existe.

    :param carpeta: Ruta de la carpeta a verificar.
    :return: True si existe, False en caso contrario.
    """
    return os.path.exists(path_folder) and os.path.isdir(path_folder)

def mkdir_src(path_folder):
    """
    Crea una carpeta si no existe.

    :param ruta_carpeta: Ruta de la carpeta a crear.
    """
    try:
        os.makedirs(path_folder, exist_ok=True)  # `exist_ok=True` evita errores si ya existe
    except Exception as e:
        print(f"Error al crear la carpeta '{ruta_carpeta}': {e}")

def is_folder_empty(path_folder):
    """
    Verifica si una carpeta está vacía.

    :param ruta_carpeta: Ruta de la carpeta a verificar.
    :return: True si está vacía, False si contiene archivos o subcarpetas.
    """
    try:
        # Listamos el contenido de la carpeta y verificamos si está vacío
        return len(os.listdir(path_folder)) == 0
    except FileNotFoundError:
        print(f"Error: La carpeta '{path_folder}' no existe.")
        return False
    except Exception as e:
        print(f"Error al verificar la carpeta '{path_folder}': {e}")
        return False

def size_pickle_file(pickefile):
    i = 0
    while True:
        try:
          # Leer un objeto del archivo fuente
          obj = pickle.load(pickefile)
          i += 1
        except EOFError:
          pickefile.seek(0)
          # Se alcanza el final del archivo fuente, se termina el bucle
          break
    return i

def size_pickle_file_closed(path_file):
    with open(path_file, 'rb') as src_file:
        i = 0
        while True:
            try:
              # Leer un objeto del archivo fuente
              obj = pickle.load(src_file)
              i += 1
            except EOFError:
              src_file.seek(0)
              # Se alcanza el final del archivo fuente, se termina el bucle
              break
    return i

def clear_picke_file(filename):
  with open(filename, 'wb') as file:
      pass

def exist_src_file(filename):
    return os.path.isfile(filename)

def is_file_empty(filename):
    return os.path.getsize(filename) == 0

def delete_file(file_to_delete):
  try:
    os.remove(file_to_delete)
  except FileNotFoundError:
    pass

def get_smiles_from_pickle_file(file_name, name_output):
    with open(file_name, 'rb') as file, open(name_output, 'w', encoding='utf-8') as file2:
        while True:
            try:
                datos = pickle.load(file)
                file2.write(f"{datos.smiles}\n")
            except EOFError:
                break
    delete_file(file_name)

def get_list_smiles_from_pickle_file(file_name):
    list_smiles = []
    with open(file_name, 'rb') as file:
        while True:
            try:
                datos = pickle.load(file)
                list_smiles.append(datos.smiles)
            except EOFError:
                break
    return list_smiles

def create_file_pkl(filename):
    with open(filename, "wb") as file:
        pass  # No se escribe nada, el archivo queda vacío

def move_file_pkl(src_file, dest_folder):
    # Mover el archivo a la carpeta de destino
    try:
        shutil.move(src_file, dest_folder)
    except FileNotFoundError:
        print(f"File '{src_file}' does not exist.")
    except PermissionError:
        print("You do not have permission to move this file.")
    except Exception as e:
        print(f"Error occurred: {e}")

def copy_file_pkl(path_src, path_dest, delete_sourse = False):
    """
    Copia un archivo .pkl desde una dirección de origen a una nueva dirección con un nombre especificado.

    Parámetros:
    origen (str): Ruta completa del archivo .pkl original.
    destino (str): Ruta completa del archivo copiado, incluyendo el nuevo nombre.

    Retorna:
    str: Mensaje indicando el éxito de la operación.
    """
    try:
        # Copiar el archivo al destino
        shutil.copy(path_src, path_dest)
        if delete_sourse:
            delete_file(source_filename)
    except FileNotFoundError:
        return "Error: El archivo de origen no fue encontrado."
    except Exception as e:
        return f"Error durante la copia del archivo: {e}"

class smilx_hydrocarbons:
    def __init__(self, cycle_pi_system, parameters):
        self.folder_src = f'dependences/valence_4/{parameters.n_heavy_atoms}'
        self.src_file_target = f'{cycle_pi_system.double_bonds}-{cycle_pi_system.triple_bonds}-{cycle_pi_system.cycles}.pkl'
        self.path_src_target = f'{self.folder_src}/{self.src_file_target}'
        self.code_target = np.array([cycle_pi_system.double_bonds, cycle_pi_system.triple_bonds, cycle_pi_system.cycles])
        self.find_src_file()
        if self.path_src_file_nearest == None:
            self.get_all_smiles_alkanes(parameters.syntax_rules, parameters.n_heavy_atoms)
#-----------------------------------------------------------------------------------------------
    def get_all_smiles_alkanes(self, syntax_rules, n_heavy_atoms):
        """
        def filter_smiles_alkanes(src_filename, dest_filename):
          with open(src_filename, 'rb') as src_file, open(dest_filename, 'ab') as dest_file:
            reg_canon_smiles = set()
            while True:
              try:
                i_smiles = pickle.load(src_file)
                canon_smiles = Chem.CanonSmiles(i_smiles.smiles)
                if canon_smiles not in reg_canon_smiles:
                  reg_canon_smiles.add(canon_smiles)
                  pickle.dump(i_smiles, dest_file)
              except EOFError:
                break"""
        
        def filter_smiles_alkanes(src_filename, dest_filename):
            with open(src_filename, 'rb') as src_file, open(dest_filename, 'ab') as dest_file:
                unique_molecules = []  # Lista de moléculas ya registradas
        
                while True:
                    try:
                        i_smiles = pickle.load(src_file)  # Cargar objeto del archivo pickle
                        mol = Chem.MolFromSmiles(i_smiles.smiles)  # Convertir a RDKit Mol
        
                        # Verificar si ya existe una estructura equivalente en unique_molecules
                        is_unique = all(not mol.HasSubstructMatch(registered_mol) or 
                                        not registered_mol.HasSubstructMatch(mol) 
                                        for registered_mol in unique_molecules)
        
                        if is_unique:
                            unique_molecules.append(mol)  # Guardar la nueva molécula única
                            pickle.dump(i_smiles, dest_file)  # Guardar objeto en el archivo destino
        
                    except EOFError:
                        break  # Fin del archivo
                  
        src_filename = "alkanes_0.pkl"
        dest_filename = "alkanes_1.pkl"
    
        with open(src_filename, "wb") as src_file:
          new_smiles = standard_smiles(n_heavy_atoms)
          pickle.dump(new_smiles, src_file)
            
        create_file_pkl(dest_filename)
    
        for i_pos in tqdm(range(len(syntax_rules)), desc= 'getting smiles alkanes'):
            
              i_rule = syntax_rules[i_pos]
        
              with open(src_filename, 'rb') as src_file, open(dest_filename, 'wb') as dest_file:
                  progress_bar = tqdm(total = size_pickle_file(src_file),
                                      desc = f'inserting C {i_pos + 1}',
                                      position = 1,
                                      leave = False)
                  while True:
                    try:
                    
                      smiles = pickle.load(src_file)
                      new_smiles = smiles.replicate(i_rule)
                    
                      for i_smiles in new_smiles:
                        pickle.dump(i_smiles, dest_file)
                    
                      #progress_bar.update(1)
                    
                    except EOFError:
                      break
              #progress_bar.close()
              clear_picke_file(src_filename)
              src_filename, dest_filename = dest_filename, src_filename

        if is_file_empty(dest_filename):
          filter_smiles_alkanes(src_filename, dest_filename)
          delete_file(src_filename)
          os.rename(dest_filename, '0-0-0.pkl')
        else:
          filter_smiles_alkanes(dest_filename, src_filename)
          delete_file(dest_filename)
          os.rename(src_filename, '0-0-0.pkl')
            
        move_file_pkl('0-0-0.pkl', self.folder_src)
        self.path_src_file_nearest = self.folder_src + "/0-0-0.pkl"
        self.nearest_code = np.array([0, 0, 0])

#-----------------------------------------------------------------------------------------------------------------------
    def get_nearest_file(self, list_files, final_code):
        self.path_src_file_nearest = ''
        self.nearest_code = tuple()
        
        for i_file in list_files:
            initial_code = np.array([int(i_str) for i_str in i_file.split('-')])
            delta_code = final_code - initial_code
            if np.all(delta_code >= 0):
                if self.nearest_code != tuple():
                    if np.linalg.norm(delta_code) < self.nearest_code[1]:
                        self.path_src_file_nearest = f'{self.folder_src}/{i_file}.pkl'
                        self.nearest_code = (initial_code, np.linalg.norm(delta_code))
                else:
                    self.path_src_file_nearest = f'{self.folder_src}/{i_file}.pkl'
                    self.nearest_code = (initial_code, np.linalg.norm(delta_code))
        self.nearest_code = self.nearest_code[0]

    def find_src_file(self):
        if not(exist_src_file(self.path_src_target)):
            
            if not(check_folder_src(self.folder_src)):
                mkdir_src(self.folder_src)
                self.path_src_file_nearest = None
                self.nearest_code = None
            elif not(is_folder_empty(self.folder_src)):
                try:
                    files = list_files(self.folder_src)
                    self.get_nearest_file(files, self.code_target)
                except:
                    self.path_src_file_nearest = None
                    self.nearest_code = None
            else:
                self.path_src_file_nearest = None
                self.nearest_code = None
        else:
            self.path_src_file_nearest = f'{self.folder_src}/{self.src_file_target}'
            self.nearest_code = self.code_target

#-----------------------------------------------------------------------------------------------
class smilx_dehydrogenation:
    def __init__(self, hydrocarbons):
        self.folder_src = hydrocarbons.folder_src
        self.src_file_target = hydrocarbons.src_file_target
        self.code_target = hydrocarbons.code_target
        self.path_src_file_nearest = hydrocarbons.path_src_file_nearest
        self.nearest_code = hydrocarbons.nearest_code
        if not(np.array_equal(self.nearest_code, self.code_target)):
            #-------------------------------------------------------------------------------------------------
            count_double_bonds = self.code_target[0] - self.nearest_code[0]
            count_triple_bonds = self.code_target[1] - self.nearest_code[1]
            count_cycle_bonds = self.code_target[2] - self.nearest_code[2]
            #-------------------------------------------------------------------------------------------------
            if count_double_bonds > 0 :
              path_src_filename = self.path_src_file_nearest
              for iteration in tqdm(range(count_double_bonds), desc = "getting smiles with double bonds"):
                self.nearest_code[0] += 1
                dest_filename = f"{self.nearest_code[0]}-{self.nearest_code[1]}-{self.nearest_code[2]}.pkl"
                path_dest_filename = f"{self.folder_src}/{dest_filename}"
                self.replicate_smiles(path_src_filename,
                                 path_dest_filename,
                                 iteration,
                                 replication = 0)
                path_src_filename = path_dest_filename
              self.path_src_file_nearest = path_dest_filename
            #-------------------------------------------------------------------------------------------------
            if count_triple_bonds > 0 :
              path_src_filename = self.path_src_file_nearest
              for iteration in tqdm(range(count_triple_bonds), desc = "getting smiles with triple bonds"):
                self.nearest_code[1] += 1
                dest_filename = f"{self.nearest_code[0]}-{self.nearest_code[1]}-{self.nearest_code[2]}.pkl"
                path_dest_filename = f"{self.folder_src}/{dest_filename}"
                self.replicate_smiles(path_src_filename,
                                 path_dest_filename,
                                 iteration,
                                 replication = 1)
                path_src_filename = path_dest_filename
              self.path_src_file_nearest = path_dest_filename
            #-------------------------------------------------------------------------------------------------
            if count_cycle_bonds > 0 :
              path_src_filename = self.path_src_file_nearest
              for iteration in tqdm(range(count_cycle_bonds), desc = "getting smiles with cycles"):
                self.nearest_code[2] += 1
                dest_filename = f"{self.nearest_code[0]}-{self.nearest_code[1]}-{self.nearest_code[2]}.pkl"
                path_dest_filename = f"{self.folder_src}/{dest_filename}"
                self.replicate_smiles(path_src_filename,
                                 path_dest_filename,
                                 iteration,
                                 replication = 2)
                path_src_filename = path_dest_filename
              self.path_src_file_nearest = path_dest_filename

    def replicate_smiles(self, src_filename, dest_filename, iteration, replication = 0):
      """
      0 = .replicate_simple_dehydrogenation()
      1 = .replicate_double_dehydrogenation()
      2 = .replicate_cycling()
      3 = .replicate_replacing_atoms()
      """
      label = {0: "Inserting double bond",
               1: "Inserting triple bond",
               2: "Inserting cycle",
               3: "Inserting atom"}
      with open(src_filename, 'rb') as src_file, open(dest_filename, 'wb') as dest_file:
        progress_bar = tqdm(total = size_pickle_file(src_file),
                            desc = f'{label[replication]} {iteration + 1}',
                            position = 1,
                            leave = False)
        reg_canon_smiles = set()
        while True:
          try:
            smiles = pickle.load(src_file)
            if replication == 0:
              new_smiles = smiles.replicate_simple_dehydrogenation()
            elif replication == 1:
              new_smiles = smiles.replicate_double_dehydrogenation()
            elif replication == 2:
              new_smiles = smiles.replicate_cycling()
            for new_smile in new_smiles:
              mol = Chem.MolFromSmiles(new_smile.smiles, sanitize = False)
              canon_smiles = Chem.MolToSmiles(mol, isomericSmiles = True, canonical = True)
              if canon_smiles not in reg_canon_smiles:
                reg_canon_smiles.add(canon_smiles)
                pickle.dump(new_smile, dest_file)
            #progress_bar.update(1)
          except EOFError:
            break
        #progress_bar.close()

    def save_path_src_file_nearest(self, dest_filename):
      with open(self.path_src_file_nearest, 'rb') as src_file, open(dest_filename, 'ab') as dest_file:
        progress_bar = tqdm(total = size_pickle_file(src_file),
                            desc = "saving smiles",
                            position = 1,
                            leave = False)
        while True:
          try:
            smiles = pickle.load(src_file)
            pickle.dump(smiles, dest_file)
            #progress_bar.update(1)
          except EOFError:
            break
        #progress_bar.close()

#----------------------------------------------------------------------------------------------
class smilx_atom_substitution:
    def __init__(self, dehydrogenation, extended_molecular_formula, parameters):
        path_out_filename = f"{parameters.filename_output_pkl}"
        path_src_filename = f"0_{parameters.filename_output_pkl}"
        path_dest_filename = f"1_{parameters.filename_output_pkl}"
        #-------------------------------------------------------------------------------------------------
        copy_file_pkl(dehydrogenation.path_src_file_nearest, path_src_filename)
        create_file_pkl(path_dest_filename)
        #-------------------------------------------------------------------------------------------------
        iteration = 0
        #-------------------------------------------------------------------------------------------------
        count_heteroatoms = parameters.n_heavy_atoms - parameters.molecular_formula['C']
        #-------------------------------------------------------------------------------------------------
        for iteration in tqdm(range(count_heteroatoms), desc = "Replacing atoms", leave = True):
            self.replicate_replacing(path_src_filename,
                                     path_dest_filename,
                                     extended_molecular_formula,
                                     iteration)
            iteration += 1
            if iteration < count_heteroatoms:
                clear_picke_file(path_src_filename)
                path_src_filename, path_dest_filename = path_dest_filename, path_src_filename

        if not is_file_empty(path_dest_filename):
            path_src_filename = path_dest_filename

        reg_canon_smiles = {}
        with open(path_src_filename, 'rb') as src_file, open(path_out_filename, 'ab') as dest_file:
            while True:
              try:
                smiles = pickle.load(src_file)
                canon_smiles = Chem.CanonSmiles(smiles.smiles)

                # Verify valid stoichiometry
                out_fm = []
                for i_element in 'C', 'N', 'O', 'S', 'B', 'P', 'F', 'I', 'Cl', 'Br':
                    out_fm.append(smiles.atoms.count(i_element))

                if canon_smiles not in reg_canon_smiles and out_fm == parameters.out_fm:
                    reg_canon_smiles[canon_smiles] = 0
                    pickle.dump(smiles, dest_file)
                    
              except EOFError:
                break

        delete_file(f"0_{parameters.filename_output_pkl}")
        delete_file(f"1_{parameters.filename_output_pkl}")
                    
    def replicate_replacing(self, src_filename, dest_filename, molecular_formula, iteration):
      with open(src_filename, 'rb') as src_file, open(dest_filename, 'ab') as dest_file:
        progress_bar = tqdm(total = size_pickle_file(src_file),
                            desc = f'"Inserting atom" {iteration + 1}',
                            position = 1,
                            leave = False)
        reg_canon_smiles = set()
        while True:
          try:
            smiles = pickle.load(src_file)
            if smiles.molecular_formula == None:
                smiles.molecular_formula = copy.deepcopy(molecular_formula)
            new_smiles = smiles.replicate_replacing_atoms()
            for new_smile in new_smiles:
              mol = Chem.MolFromSmiles(new_smile.smiles, sanitize = False)
              canon_smiles = Chem.MolToSmiles(mol, isomericSmiles = True, canonical = True)
              if canon_smiles not in reg_canon_smiles:
                reg_canon_smiles.add(canon_smiles)
                pickle.dump(new_smile, dest_file)
            #progress_bar.update(1)
          except EOFError:
            break
        #progress_bar.close()
          
#----------------------------------------------------------------------------------------------
class chemical_space_classic:
    def __init__(self, parameters):
        dest_filename = parameters.filename_output_pkl
        create_file_pkl(dest_filename)

        for i_systems in parameters.cycles_pi_systems:
            if parameters.molecular_formula["hdi"] == i_systems.double_bonds + 2*i_systems.triple_bonds + i_systems.cycles:
                
                self.smx_hydrocarbons = smilx_hydrocarbons(i_systems, parameters)
                
                self.smx_dehydrogenation = smilx_dehydrogenation(self.smx_hydrocarbons)
                
                src_filename = self.smx_dehydrogenation.path_src_file_nearest
                
                if parameters.n_heavy_atoms == parameters.molecular_formula["C"]:
                    self.smx_dehydrogenation.save_path_src_file_nearest(dest_filename)
                else:
                    smilx_atom_substitution(self.smx_dehydrogenation, 
                                            parameters.molecular_formula, 
                                            parameters)
        count_smiles = size_pickle_file_closed(parameters.filename_output_pkl)
        list_smiles = get_list_smiles_from_pickle_file(parameters.filename_output_pkl)
        get_smiles_from_pickle_file(parameters.filename_output_pkl, parameters.filename_output_smi)
        st.write(f"******************************Exploration completed: {count_smiles} isomers found******************************")
        with open(f"{parameters.filename_output_smi}", "r") as file:
            st.download_button(
                label="Download SMILES",
                data=file,
                file_name=f"{parameters.filename_output_smi}",
                mime="text/smi",
                )
        df = pd.DataFrame({"smi": list_smiles, "id": range(1, len(list_smiles) + 1)})
        mg = mols2grid.display(df, smiles_col="smi", subset=["id", "img", "smi"], n_cols=6, size = (130, 90))        
        html_grid = mg.data
        st.components.v1.html(html_grid, height=600, scrolling=True)

#-------------------------------------------------------------------------------------------------------------------------Carbenes
def filter_canonical_smiles(list_smiles_carbened):
    canonical_smiles = [
        Chem.CanonSmiles("".join(i_smiles.smiles))
        for i_smiles in list_smiles_carbened
    ]

    df_smiles = pd.DataFrame({
        "smiles": list_smiles_carbened,
        "canonical_smiles": canonical_smiles
    })

    df_smiles = df_smiles.drop_duplicates(subset=["canonical_smiles"])
    df_smiles.reset_index(drop=True, inplace=True)

    return list(df_smiles["smiles"])


def get_list_carbenated_formulas(molecular_formula):
    molecular_formula['[C]'] = 0
    list_new_formulas = [molecular_formula]

    if molecular_formula['C'] > 0 and molecular_formula['hdi'] > 0:
        new_formula = copy.deepcopy(molecular_formula)

        while new_formula['hdi'] > 0 and new_formula['C'] > 0:
            new_formula['hdi'] -= 1
            new_formula['C'] -= 1
            new_formula['[C]'] += 1

            list_new_formulas.append(copy.deepcopy(new_formula))

    return list_new_formulas
#------------------------------------------------------------------------------------------------

def get_all_substitutions(smiles):

    def get_atoms_from_molecular_formula(molecular_formula):
        list_atoms = []

        for i_atom in molecular_formula:
            if (
                molecular_formula[i_atom] != 0
                and i_atom != "H"
                and i_atom != "hdi"
            ):
                list_atoms.append(i_atom)

        return list_atoms

    list_substitutions_0 = []
    list_substitutions_1 = []

    valences = {
        "C": 4,
        "O": 2,
        "S": 2,
        "[C]": 2,
        "N": 3,
        "P": 3,
        "B": 3,
        "Cl": 1,
        "Br": 1,
        "I": 1,
        "F": 1,
    }

    for pos in range(len(smiles.atoms)):

        if pos == 0:
            atoms = get_atoms_from_molecular_formula(smiles.molecular_formula)

            for atom in atoms:
                if valences[atom] >= smiles.degrees[pos]:
                    new_smiles = copy.deepcopy(smiles)
                    new_smiles.substitution_carbon_dehydrogenation(atom, pos)
                    list_substitutions_0.append(copy.deepcopy(new_smiles))

        else:

            if not list_substitutions_1:
                for j_smiles in list_substitutions_0:

                    atoms = get_atoms_from_molecular_formula(j_smiles.molecular_formula)

                    for i_atom in atoms:
                        if valences[i_atom] >= j_smiles.degrees[pos]:
                            new_smiles = copy.deepcopy(j_smiles)
                            new_smiles.substitution_carbon_dehydrogenation(i_atom, pos)
                            list_substitutions_1.append(copy.deepcopy(new_smiles))

                list_substitutions_0 = []

            else:
                for j_smiles in list_substitutions_1:

                    atoms = get_atoms_from_molecular_formula(j_smiles.molecular_formula)

                    for i_atom in atoms:
                        if valences[i_atom] >= j_smiles.degrees[pos]:
                            new_smiles = copy.deepcopy(j_smiles)
                            new_smiles.substitution_carbon_dehydrogenation(i_atom, pos)
                            list_substitutions_0.append(copy.deepcopy(new_smiles))

                list_substitutions_1 = []

    return list_substitutions_0 + list_substitutions_1


def get_list_substitutions(list_smiles):

    list_substitutions = []

    for i_smiles in list_smiles:
        list_substitutions += get_all_substitutions(i_smiles)
    return filter_canonical_smiles(list_substitutions)
#------------------------------------------------------------------------------------------------

def get_possible_cycles(smiles):
  list_possible_cycle = []

  if ')' in smiles.smiles[-2]:
      for i_pos in range(len(smiles.atoms) - 1):
          for j_pos in range(i_pos + 2, len(smiles.atoms)):  # get cycle (i,j)

              if smiles.type_smiles == 'Lineal':
                  if (
                      smiles.hydrogens[i_pos] > 0
                      and smiles.hydrogens[j_pos] > 0
                      and (i_pos, j_pos) not in smiles.bonds
                  ):
                      list_possible_cycle.append((i_pos, j_pos))

              else:
                  if (
                      smiles.hydrogens[i_pos] > 0
                      and smiles.hydrogens[j_pos] > 0
                      and (i_pos, j_pos) not in smiles.bonds
                      and (
                          smiles.degrees[i_pos] != 1
                          or smiles.degrees[j_pos] != 1
                      )
                  ):
                      list_possible_cycle.append((i_pos, j_pos))

  else:
      for i_pos in range(len(smiles.atoms) - 2):
          for j_pos in range(i_pos + 2, len(smiles.atoms)):

              if smiles.type_smiles == 'Lineal':
                  if (
                      smiles.hydrogens[i_pos] > 0
                      and smiles.hydrogens[j_pos] > 0
                      and (i_pos, j_pos) not in smiles.bonds
                  ):
                      list_possible_cycle.append((i_pos, j_pos))

              else:
                  if (
                      smiles.hydrogens[i_pos] > 0
                      and smiles.hydrogens[j_pos] > 0
                      and (i_pos, j_pos) not in smiles.bonds
                      and (
                          smiles.degrees[i_pos] != 1
                          or smiles.degrees[j_pos] != 1
                      )
                  ):
                      list_possible_cycle.append((i_pos, j_pos))

  return list_possible_cycle


def get_all_possible_cycles(smiles):
    new_list_smiles_0, new_list_smiles_1 = [], []

    list_cycles = get_possible_cycles(smiles)
    list_cycles = dict(zip(range(1, len(list_cycles) + 1), list_cycles))

    r = smiles.molecular_formula['hdi']
    deep = len(list_cycles) - r + 1
    flag_cycles = 0

    while deep <= len(list_cycles):
        if flag_cycles == 0:
            for index in range(1, deep + 1):
                if (
                    smiles.hydrogens[list_cycles[index][0]] > 0
                    and smiles.hydrogens[list_cycles[index][1]] > 0
                ):
                    new_smiles = copy.deepcopy(smiles)
                    new_smiles.cycle(list_cycles[index], 1)
                    new_smiles.index_cycles.append(index)
                    new_list_smiles_0.append(copy.deepcopy(new_smiles))
            flag_cycles += 1

        else:
            if not new_list_smiles_1:
                for i_smiles in new_list_smiles_0:
                    for index in range(i_smiles.index_cycles[-1] + 1, deep + 1):
                        if (
                            i_smiles.hydrogens[list_cycles[index][0]] > 0
                            and i_smiles.hydrogens[list_cycles[index][1]] > 0
                        ):
                            new_smiles = copy.deepcopy(i_smiles)
                            new_smiles.cycle(list_cycles[index], 1)
                            new_smiles.index_cycles.append(index)
                            new_list_smiles_1.append(copy.deepcopy(new_smiles))
                new_list_smiles_0 = []

            else:
                for i_smiles in new_list_smiles_1:
                    for index in range(i_smiles.index_cycles[-1] + 1, deep + 1):
                        if (
                            i_smiles.hydrogens[list_cycles[index][0]] > 0
                            and i_smiles.hydrogens[list_cycles[index][1]] > 0
                        ):
                            new_smiles = copy.deepcopy(i_smiles)
                            new_smiles.cycle(list_cycles[index], 1)
                            new_smiles.index_cycles.append(index)
                            new_list_smiles_0.append(copy.deepcopy(new_smiles))
                new_list_smiles_1 = []

        r -= 1
        deep = len(list_cycles) - r + 1

    return new_list_smiles_0 + new_list_smiles_1

def get_list_cycled_smiles(list_smiles):
    list_new_smiles = []

    for i_smiles in list_smiles:
        list_new_smiles += get_all_possible_cycles(i_smiles)

    return filter_canonical_smiles(list_new_smiles)
#------------------------------------------------------------------------------------------------
def get_all_possibles_dehydrogenations(smiles, bond):
    list_possible_dehydrogenations = []
    new_smiles = copy.deepcopy(smiles)

    while (
        new_smiles.hydrogens[bond[0]] > 0
        and new_smiles.hydrogens[bond[1]] > 0
        and new_smiles.molecular_formula['hdi'] > 0
    ):
        new_smiles.dehydrogenate(bond)
        list_possible_dehydrogenations.append(copy.deepcopy(new_smiles))

    return list_possible_dehydrogenations


def get_smiles_dehydrogenates(smiles):
    # ---------------------------------------------------------------------
    def clear_by_prune(list_to_prune, list_smiles_dehydrogenates):
        i = 0
        while i < len(list_to_prune):
            if list_to_prune[i].molecular_formula['hdi'] == 0:
                list_smiles_dehydrogenates.append(copy.deepcopy(list_to_prune[i]))
                list_to_prune.remove(list_to_prune[i])
            else:
                i += 1
    # ---------------------------------------------------------------------
    list_smiles_1, list_smiles_2, flag = [], [], 0

    for i_bond in smiles.bonds:
        if flag == 0:
            list_smiles_0 = [copy.deepcopy(smiles)]
            list_smiles_0 += get_all_possibles_dehydrogenations(smiles, i_bond)
            clear_by_prune(list_smiles_0, list_smiles_2)
            flag = 1
        else:
            if list_smiles_1 == []:
                for j_smiles in list_smiles_0:
                    list_smiles_1.append(copy.deepcopy(j_smiles))
                    list_smiles_1 += get_all_possibles_dehydrogenations(j_smiles, i_bond)
                clear_by_prune(list_smiles_1, list_smiles_2)
                list_smiles_0 = []
            else:
                for k_smiles in list_smiles_1:
                    list_smiles_0.append(copy.deepcopy(k_smiles))
                    list_smiles_0 += get_all_possibles_dehydrogenations(k_smiles, i_bond)
                clear_by_prune(list_smiles_0, list_smiles_2)
                list_smiles_1 = []

    return list_smiles_2 + list_smiles_0 + list_smiles_1


def get_list_smiles_dehydrogenates(list_smiles):

    list_smiles_dehydrogenates = []

    for i_smiles in list_smiles:

        list_smiles_dehydrogenates += get_smiles_dehydrogenates(i_smiles)

    return filter_canonical_smiles(list_smiles_dehydrogenates)

#--------------------------------------------------------------------------------------------------
def get_connectivity_lineal(tokenSMILES, nesting_levels):
    list_lineal_connectivity = []

    for i_level in range(len(nesting_levels)):
        if ')' in tokenSMILES[i_level]:
            level -= 1
            continue
        else:
            level = nesting_levels[i_level]

            for j_level in range(i_level + 1, len(nesting_levels)):

                if nesting_levels[j_level] == nesting_levels[i_level]:

                    if '=' in tokenSMILES[j_level]:
                        list_lineal_connectivity.append([i_level, j_level, 2])

                    elif '#' in tokenSMILES[j_level]:
                        list_lineal_connectivity.append([i_level, j_level, 3])

                    else:
                        list_lineal_connectivity.append([i_level, j_level, 1])

                    break

                else:

                    if level == nesting_levels[i_level] and '(' in tokenSMILES[j_level]:
                        level += 1

                        if '=' in tokenSMILES[j_level]:
                            list_lineal_connectivity.append([i_level, j_level, 2])

                        elif '#' in tokenSMILES[j_level]:
                            list_lineal_connectivity.append([i_level, j_level, 3])

                        else:
                            list_lineal_connectivity.append([i_level, j_level, 1])

                        if ')' in tokenSMILES[j_level]:
                            level -= 1

                    else:

                        if level != nesting_levels[i_level] and '(' in tokenSMILES[j_level]:
                            level += 1

                        if level != nesting_levels[i_level] and ')' in tokenSMILES[j_level]:
                            level -= 1

    return list_lineal_connectivity


def nesting_level_smiles(tokenSMILES):

    """Return the nesting level for each token in a TokenSMILES."""
    list_levels = []
    level = 0

    for i_word in tokenSMILES:
        if '(' not in i_word and ')' not in i_word:
            list_levels.append(level)

        else:
            if '(' in i_word and ')' not in i_word:
                level += 1
                list_levels.append(level)

            elif '(' in i_word and ')' in i_word:
                level += 1
                list_levels.append(level)
                level -= 1

            elif '(' not in i_word and ')' in i_word:
                list_levels.append(level)
                level -= 1

    return list_levels


def list_hydrogens(tokenSMILES, list_connectivity):
    list_total_hydrogens = []

    for i_word in tokenSMILES:
        if 'Cl' in i_word or 'Br' in i_word or 'F' in i_word or 'I' in i_word:
            list_total_hydrogens.append(1)

        else:
            if 'C' in i_word:
                if '[CH]' in i_word or '[C]' in i_word:
                    list_total_hydrogens.append(2)
                else:
                    list_total_hydrogens.append(4)

            elif 'N' in i_word or 'P' in i_word or 'B' in i_word:
                list_total_hydrogens.append(3)

            elif 'O' in i_word or 'S' in i_word:
                list_total_hydrogens.append(2)


    list_bonds = []
    bond = 0

    for i in range(len(tokenSMILES)):
        for connectivity in list_connectivity:
            if i == connectivity[0] or i == connectivity[1]:
                bond += connectivity[2]

        list_bonds.append(bond)
        bond = 0

    return np.array(list_total_hydrogens) - np.array(list_bonds)

#-------------------------------------------------------------------------------------------------
def get_new_list_branches(old_branch, limit_deep):
    new_list_branches = []
    resto_smiles = limit_deep - len(old_branch)
    count_three = old_branch.count("(C") - old_branch.count("C)")

    if "(C" not in old_branch:
        # ------------------------------------------------------ add 0
        copy_branch = copy.deepcopy(old_branch)
        copy_branch.append("C")
        new_list_branches.append(copy_branch)

        # ------------------------------------------------------ add 1
        if (
            len(old_branch) > 1
            and (
                (old_branch[-2] == old_branch[-1] != "(C)")
                or (old_branch[-2] != old_branch[-1])
            )
        ):
            copy_branch = copy.deepcopy(old_branch)
            copy_branch.append("(C)")
            new_list_branches.append(copy_branch)
        elif len(old_branch) < 2:
            copy_branch = copy.deepcopy(old_branch)
            copy_branch.append("(C)")
            new_list_branches.append(copy_branch)

        # ------------------------------------------------------ add 2
        if resto_smiles >= 2:
            if (
                len(old_branch) > 1
                and (
                    (old_branch[-2] == old_branch[-1] != "(C)")
                    or (old_branch[-2] != old_branch[-1])
                )
            ):
                copy_branch = copy.deepcopy(old_branch)
                copy_branch.append("(C")
                new_list_branches.append(copy_branch)
            elif len(old_branch) < 2:
                copy_branch = copy.deepcopy(old_branch)
                copy_branch.append("(C")
                new_list_branches.append(copy_branch)

    else:
        # ------------------------------------------------------ add 0
        if count_three == 0:
            copy_branch = copy.deepcopy(old_branch)
            copy_branch.append("C")
            new_list_branches.append(copy_branch)
        elif resto_smiles - count_three >= 1:
            copy_branch = copy.deepcopy(old_branch)
            copy_branch.append("C")
            new_list_branches.append(copy_branch)

        # ------------------------------------------------------ add 1
        if count_three == 0:
            copy_branch = copy.deepcopy(old_branch)
            copy_branch.append("(C)")
            smiles = ["C", "C", *copy_branch, "C"]

            if (
                np.all(
                    list_hydrogens(
                        smiles,
                        get_connectivity_lineal(
                            smiles,
                            nesting_level_smiles(smiles)
                        )
                    ) >= 0
                )
                is True
            ):
                new_list_branches.append(copy_branch)

        elif resto_smiles - count_three >= 1:
            copy_branch = copy.deepcopy(old_branch)
            copy_branch.append("(C)")
            new_list_branches.append(copy_branch)

        # ------------------------------------------------------ add 2
        if len(old_branch) > 1:
            if (
                count_three == 0
                and resto_smiles >= 2
                and (
                    (old_branch[-2] == old_branch[-1] != "(C)")
                    or (old_branch[-2] != old_branch[-1])
                )
            ):
                copy_branch = copy.deepcopy(old_branch)
                copy_branch.append("(C")
                new_list_branches.append(copy_branch)

            elif (
                count_three != 0
                and resto_smiles >= 2
                and resto_smiles - count_three >= 2
                and (
                    (old_branch[-2] == old_branch[-1] != "(C)")
                    or (old_branch[-2] != old_branch[-1])
                )
            ):
                copy_branch = copy.deepcopy(old_branch)
                copy_branch.append("(C")
                new_list_branches.append(copy_branch)

        else:
            if count_three == 0 and resto_smiles >= 2:
                copy_branch = copy.deepcopy(old_branch)
                copy_branch.append("(C")
                new_list_branches.append(copy_branch)
            elif resto_smiles >= 2 and resto_smiles - count_three >= 2:
                copy_branch = copy.deepcopy(old_branch)
                copy_branch.append("(C")
                new_list_branches.append(copy_branch)

        # ------------------------------------------------------ add 3
        if count_three != 0:
            copy_branch = copy.deepcopy(old_branch)
            copy_branch.append("C)")

            if copy_branch.count("(C") == copy_branch.count("C)"):
                if copy_branch[0] != "C":
                    smiles = ["C", "C", *copy_branch, "C"]
                    if (
                        np.all(
                            list_hydrogens(
                                smiles,
                                get_connectivity_lineal(
                                    smiles,
                                    nesting_level_smiles(smiles)
                                )
                            ) >= 0
                        )
                        is True
                    ):
                        new_list_branches.append(copy_branch)
                else:
                    smiles = ["C", "C", *copy_branch, "C"]
                    if (
                        np.all(
                            list_hydrogens(
                                smiles,
                                get_connectivity_lineal(
                                    smiles,
                                    nesting_level_smiles(smiles)
                                )
                            ) >= 0
                        )
                        is True
                    ):
                        new_list_branches.append(copy_branch)
            else:
                new_list_branches.append(copy_branch)

    return new_list_branches


def get_possible_alkanes(molecular_formula):

    def filter_smiles_duplicates(list_smiles):

        df_smiles = pd.DataFrame({
            "smiles": list_smiles,
            "canonical": list(
                map(
                    Chem.CanonSmiles,
                    [''.join(fragment) for fragment in list_smiles]
                )
            )
        })

        df_smiles = df_smiles.drop_duplicates(
            subset=['canonical'],
            keep='first',
            inplace=False
        )

        df_smiles.reset_index(drop=True, inplace=True)

        return list(df_smiles["smiles"])

    carbons = 0

    for element in ['C', '[C]', 'N', 'O', 'S', 'B', 'P', 'F', 'Cl', 'Br', 'I']:
        carbons += molecular_formula[element]

    if carbons == 1:
        return [['C']]

    elif carbons == 2:
        return [['C', 'C']]

    elif carbons == 3:
        return [['C', 'C', 'C']]

    else:

        limit_deep = carbons - 3
        level_deep = 1

        list_0 = [[]]
        list_1 = []

        x = 0

        while level_deep <= limit_deep:

            x += 1

            if list_1 == []:

                for branch in list_0:
                    list_1 += get_new_list_branches(branch, limit_deep)

                list_0 = []

            else:

                for branch in list_1:
                    list_0 += get_new_list_branches(branch, limit_deep)

                list_1 = []

            level_deep += 1

        if list_1 == []:

            for item in list_0:
                list_1.append(['C', 'C'] + item + ['C'])

            return filter_smiles_duplicates(list_1)

        else:

            for item in list_1:
                list_0.append(['C', 'C'] + item + ['C'])

            return filter_smiles_duplicates(list_0)

def get_smiles_carened_from_list(file_name, list_smiles):
    with open(file_name, 'r') as file:
        for  i_smiles in list_smiles:
            file.write(i_smiles + "\n")

class chemical_space_carbenes:

  def __init__(self, parameters):
    #---------------------------------------------------------------------------------------- Section 1
    self.molecular_formulas_carbenes = get_list_carbenated_formulas(parameters.molecular_formula)
    #---------------------------------------------------------------------------------------- Section 2
    list_smiles_alkanes = []

    for i_alkane in get_possible_alkanes(parameters.molecular_formula):
        new_smiles = smiles_carbened(i_alkane)
        list_smiles_alkanes.append(new_smiles)
    #---------------------------------------------------------------------------------------- Section 3
    list_smiles_totals = []
    list_smiles = []

    for i_formula in self.molecular_formulas_carbenes:

        list_smiles_0, list_smiles_1 = [], []

        for i_smiles in list_smiles_alkanes:
            i_smiles.molecular_formula = copy.deepcopy(i_formula)
            list_smiles_0.append(copy.deepcopy(i_smiles))
    #------------------------------------------------------------------------------------ Section 4
        if i_formula['hdi'] > 0:

            list_smiles_0 = get_list_smiles_dehydrogenates(list_smiles_0)

            i = 0
            while i < len(list_smiles_0):
                if list_smiles_0[i].molecular_formula['hdi'] == 0:
                    list_smiles_1.append(copy.deepcopy(list_smiles_0[i]))
                    list_smiles_0.remove(list_smiles_0[i])
                else:
                    i += 1
    #------------------------------------------------------------------------------------ Section 5
            list_smiles_0 = get_list_cycled_smiles(list_smiles_0)
            list_smiles_0 = list_smiles_1 + list_smiles_0
    #------------------------------------------------------------------------------------ Section 6
        if (i_formula['O'] > 0 or i_formula['S'] > 0 or i_formula['N'] > 0 or 
            i_formula['P'] > 0 or i_formula['B'] > 0 or i_formula['Cl'] > 0 or 
            i_formula['Br'] > 0 or i_formula['I'] > 0 or i_formula['F'] > 0 or 
            i_formula['[C]'] > 0):
          
            list_smiles_0 = get_list_substitutions(list_smiles_0)
    #------------------------------------------------------------------------------------ Section 7
        list_smiles_totals += copy.deepcopy(list_smiles_0)
        for i_smiles in list_smiles_0:
          list_smiles.append(''.join(i_smiles.smiles))
    #------------------------------------------------------------------------------------ Section 8
    get_smiles_carened_from_list(parameters.filename_output_smi, list_smiles)
    st.write(f"******************************Exploration completed: {len(list_smiles)} isomers found******************************")
    with open(f"{parameters.filename_output_smi}", "r+") as file:
        st.download_button(
            label="Download SMILES",
            data=file,
            file_name=f"{parameters.filename_output_smi}",
            mime="text/smi",
            )
    df = pd.DataFrame({"smi": list_smiles, "id": range(1, len(list_smiles) + 1)})
    mg = mols2grid.display(df, smiles_col="smi", subset=["id", "img", "smi"], n_cols=6, size = (130, 90))        
    html_grid = mg.data
    st.components.v1.html(html_grid, height=600, scrolling=True)

        

