#!/usr/bin/env python
"""
Script to replace empty notebook cells with a comment so they render on jupyterbook HTML website

cell['source'] = '' -> '#Studet Exercise'

"""

from execnb.nbio import *
import glob

notebooks = glob.glob('**/*ipynb')

for path in notebooks:
    print(f'Reading {path}...')
    j = read_nb(path)
    
    empties = [c for c in j.cells if c['source'] == '']
    print(f'Replacing {len(empties)} empty cells...') 
    
    # In-place replacement of existing strings
    for empty in empties:
        empty['source'] = '#Student Exercise'
        
    write_nb(j, path)