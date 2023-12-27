import os
import sys

#Makes contents of objects file accessible
current_path = os.getcwd()
sys.path.insert(0,f'{current_path}//objects')

from arrow import arrow
from linker import linker
from reaction import reaction

def classify_molecules(input_reaction):
    print(input_reaction)
    
def get_input():
    reaction_scheme = []

    user_input = str(input("enter a reaction"))
    reagents = user_input.split(" ")

    for reagent in reagents:
        checked = False
        print("-")
        
        for potential_linker in linker.linker_types:
            if not checked and reagent == linker:
                linker_to_append = linker(potential_linker)
                reaction_scheme.append(linker_to_append())
                print("It's a plus")
                checked = True
            break

        for potential_arrow in arrow.arrow_types:
            if not checked and reagent == potential_arrow: 
                arrow_to_append = arrow(potential_arrow)
                reaction_scheme.append(arrow_to_append())
                checked = True            
            break 
        
        if not checked:
            if is_organic(reagent): 
                #Organic script
                break
            else:
                marked_character = ""
                for character in reagent: 
                    if character.isupper():
                        marked_character += "@" + character
                    else:
                        marked_character += character
                        atoms = marked_character.split("@")
                
                print(atoms)
    
def is_organic(reagent):
    length_of_longest_substring = 0 
    current_longest = 0
    for character in reagent:
        if character.isalpha() and character.islower():
            current_longest += 1
        else:
            length_of_longest_substring = current_longest
            current_longest = 0
    
    if length_of_longest_substring > 2:
        return True
        


    


            
"""
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
    else:
        reactants = user_input.split("+")
        products = None
        reaction_arrow = None

    input_reaction = reaction(reactants,reaction_arrow,products)
    
    classify_molecules(input_reaction)

    return

"""

get_input()