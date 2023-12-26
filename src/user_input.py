import os
import sys

current_path = os.getcwd()
sys.path.insert(0,f'{current_path}//objects')

from arrow import (arrow,arrow_info)
from reaction import reaction

def classify_molecules(input_reaction):
    print(input_reaction)
    
def get_input():
    user_input = str(input("enter a reaction"))
    user_input.replace(" ","")
   
    arrow_types = [["--><-", 5], ["-><--", 5], ["-><-", 4], ["->", 2], ["<-", 2]]
    arrow_index = -1

    for arrow_type in arrow_types:
        arrow_index = user_input.find(arrow_type[arrow_info.TYPE.value])
        if arrow_index != -1:
            reaction_arrow = arrow(arrow_type, arrow_index)
            break
    
    if arrow_index != -1:
        reactants = user_input[:reaction_arrow.index].split("+")
        products = user_input[reaction_arrow.index+reaction_arrow.length:].split("+")
        print(reactants)
        print(products)
    else:
        reactants = user_input.split("+")
        products = NULL
        reaction_arrow = None
        print(reactants)

    input_reaction = reaction(reactants,reaction_arrow,products)
    
    classify_molecules(input_reaction)

    return