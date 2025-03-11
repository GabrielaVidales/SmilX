import os
import numpy as np
import shutil
import pickle
import copy
from tqdm import tqdm
from smilx_chemistry_tools import standard_smiles
from rdkit import Chem
from rdkit.Chem import AllChem
import streamlit as st
import pandas as pd
import mol2grid

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
                    
                      progress_bar.update(1)
                    
                    except EOFError:
                      break
              progress_bar.close()
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
            progress_bar.update(1)
          except EOFError:
            break
        progress_bar.close()

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
            progress_bar.update(1)
          except EOFError:
            break
        progress_bar.close()

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
            
        with open(path_src_filename, 'rb') as src_file, open(path_out_filename, 'ab') as dest_file:
            while True:
              try:
                smiles = pickle.load(src_file)
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
            progress_bar.update(1)
          except EOFError:
            break
        progress_bar.close()
          
#----------------------------------------------------------------------------------------------
class chemical_space:
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
        df = pd.DataFrame({"smi": list_smiles, "id": range(1, len(list_smiles) + 1)})
        html_grid = mols2grid.display(df, smiles_col="smi", subset=["id", "img", "smi"], n_cols=3).repr_html()
        st.components.v1.html(html_grid.data, height=400, scrolling=True)
