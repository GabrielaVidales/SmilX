import re
from smilx_chemistry_tools import get_unsaturations, get_hdi
import streamlit as st

class initial_parameters:
#----------------------------------------------------------------------------------- Section 0
  def __init__(self):
    import streamlit as st

	st.markdown(
		"""
		<div style="text-align: center;">
			<img src="logo_smilx.png" width="600">
		</div>
		""", 
		unsafe_allow_html=True
	)
  
    st.write('                 CENTRO DE INVESTIGACIÓN Y ESTUDIOS AVANZADOS DEL INSTITUTO POLITÉCNICO NACIONAL (CINVESTAV)                    \n'+
             '                                                  THEOCHEM MÉRICA YUCATÁN                                                       \n'+
             '                  GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 Copyright (C) 2007 Free Software Foundation                  ')
    self.ask_molecular_formula()       # Enter molecular formula               e.g. C6H6, C2H5NO2
    self.write_name_output_file()      # Write name output file                "C6H6_Structural_isomers_without_carbenes"
    self.get_syntax_rules()            # Get syntax_rules                      [[0], [0],[0, 1], [0, 1], [0]]
    self.get_cycles_pi_systems()       # Get syntax_rules                      [[0], [0],[0, 1], [0, 1], [0]]
#----------------------------------------------------------------------------------- Section 1
  def count_atoms_from_molecular_formula(self, molecular_formula):
    self.n_heavy_atoms = 0
    for element, atoms in zip(molecular_formula.keys(), molecular_formula.values()):
      if element not in {'hdi', 'H'}:
        self.n_heavy_atoms += atoms
        
  def ask_molecular_formula(self):
    try:
      self.str_molecular_formula = st.text_input("Enter the molecular formula (e.g. C6H6, C2H5NO2): ", value="C6H14", key="first")
      self.get_molecular_formula()
      self.is_valid_molecular_formula = True
      self.count_atoms_from_molecular_formula(self.molecular_formula)
    except:
      pass
  

  def get_molecular_formula(self):
    elements_y_atoms = re.findall(r'([A-Z][a-z]*)(\d*)', self.str_molecular_formula)
    if elements_y_atoms != []:
        self.molecular_formula = dict()
        for i_tuple in elements_y_atoms:
            if i_tuple[1] == '':
                self.molecular_formula[i_tuple[0]] = 1
            else:
                self.molecular_formula[i_tuple[0]] = int(i_tuple[1])
        for i_element in 'C','H','N','O','S','B','P','F','Cl','Br','I':
            if i_element not in self.molecular_formula:
                self.molecular_formula[i_element] = 0
        self.molecular_formula['hdi'] = get_hdi(self.molecular_formula)
    else:
        self.molecular_formula = None

  def reorder_molecular_formula(self):
    self.str_molecular_formula = ''
    for i_element in 'C','H','B','Br','Cl','F','I','N','O','P','S':
      if self.molecular_formula[i_element] > 0:
        if self.molecular_formula[i_element] == 1:
          self.str_molecular_formula += f'{i_element}'
        else:
          self.str_molecular_formula += f'{i_element}{self.molecular_formula[i_element]}'
#----------------------------------------------------------------------------------- Section 2
  def write_name_output_file(self):
    self.filename_output_pkl = self.str_molecular_formula + '.pkl'
    self.filename_output_smi = self.str_molecular_formula + '.smi'
    self.filename_output_xyz = self.str_molecular_formula + '.xyz'
#----------------------------------------------------------------------------------- Section 3
  def get_syntax_rules(self):
    if self.n_heavy_atoms in {1, 2, 3}:
      self.syntax_rules = [[0] for i_atom in range(self.n_heavy_atoms)]
    elif self.n_heavy_atoms in {4, 5, 6}:
      self.syntax_rules = [[0], [0]] + [[0, 1] for i_atom in range(self.n_heavy_atoms - 3)] + [[0]]
    elif self.n_heavy_atoms == 7:
      self.syntax_rules = [[0], [0],[0, 1], [0, 1, 2], [0, 1, 3], [0, 1], [0]]
    elif self.n_heavy_atoms == 8:
      self.syntax_rules = [[0], [0],[0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 3], [0, 1], [0]]
    elif self.n_heavy_atoms > 8:
      self.syntax_rules = [[0], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
      self.syntax_rules += [[0, 1, 2, 3] for i_atom in range(self.n_heavy_atoms - 8)]
      self.syntax_rules += [[0, 1, 3], [0, 1], [0]]
#----------------------------------------------------------------------------------- Section 3
  def get_cycles_pi_systems(self):
      self.cycles_pi_systems = get_unsaturations(self.molecular_formula, self.n_heavy_atoms)

