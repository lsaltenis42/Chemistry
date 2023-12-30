from dataclasses import replace
import os
import sys
from unittest.util import unorderable_list_difference

#from macpath import split

#Makes contents of objects file accessible
current_path = os.getcwd()
sys.path.insert(0,f'{current_path}//objects')

#Imports objects 
from arrow import arrow
from linker import linker
from molecule import molecule
from reaction import reaction

def store_arrows(user_input, arrows):
    for potential_arrow in arrow.arrow_types:
        arrow_start_index = 0
        occurrences = user_input.count(potential_arrow["style"])
        for _ in range(occurrences):
            arrow_start_index = user_input.index(potential_arrow["style"])
            arrow_end_index = arrow_start_index + potential_arrow["length"]-1
            before_caption = ""
            after_caption = ""
            
            if user_input[arrow_start_index-1] == "\"": #Checks if caption exists before arrow
                sub_string = user_input[:arrow_start_index-1]
                sub_string = sub_string[::-1] #sub_string is reversed
                second_quotation_mark_index = arrow_start_index - 1 - sub_string.index("\"") - 1
                before_caption = user_input[second_quotation_mark_index:arrow_start_index]
                arrow_start_index = second_quotation_mark_index

            if arrow_end_index < len(user_input) and user_input[arrow_end_index+1] == "\"": #Checks if caption exists after arrow
                sub_string = user_input[arrow_end_index+2:]
                second_quotation_mark_index = arrow_end_index+2 + sub_string.index("\"")
                after_caption = user_input[arrow_end_index+1:second_quotation_mark_index]
                arrow_end_index = second_quotation_mark_index

            arrow_to_append = arrow(potential_arrow["style"], arrow_start_index, before_caption, after_caption)
            arrows.append(arrow_to_append)
            configured_substring = user_input[arrow_start_index:arrow_end_index].replace(user_input[arrow_start_index:arrow_end_index],"$")
            user_input = user_input[:arrow_start_index] + configured_substring + user_input[arrow_end_index:]
            
            

    for i, item in enumerate(arrows):
        for j in arrows:
            caption_range = j.caption_index_range()
            if (item.index > caption_range["before"]["start_index"] and item.index < caption_range["before"]["end_index"]) or (item.index > caption_range["after"]["start_index"] and item.index < caption_range["after"]["end_index"]):
                arrows.pop(i)
    
    for n in arrows:
        print(n.type)
        print(n.index)
        print(n.caption["before"])
        print(n.caption["after"])
    
    return user_input
"""
def store_arrows(user_input, arrows):
    for potential_arrow in arrow.arrow_types:
        arrow_start_index = 0
        occurrences = user_input.count(potential_arrow["first_part"])
        if occurrences != 0:
            for _ in range(occurrences):
                arrow_start_index = user_input[arrow_start_index:].index(potential_arrow["first_part"])
                caption_start_index = arrow_start_index+potential_arrow["caption_start_index"]
                try:
                    caption_end_index = user_input.index(potential_arrow["last_part"],arrow_start_index)
                except :
                    continue
                
                arrow_type = potential_arrow["first_part"]+potential_arrow["last_part"]
                caption = user_input[caption_start_index:caption_end_index].strip()
                current_arrow = arrow(arrow_type, caption, arrow_start_index)
                arrow_end_index = caption_end_index + potential_arrow["lenght_after_caption"]
                arrow_length = arrow_end_index - arrow_start_index
                try:
                    store_arrows(user_input[caption_start_index:caption_end_index], arrows).index("@")
                except:
                    user_input = user_input.replace(user_input[arrow_start_index:arrow_end_index], "@") 
                    arrows.append(current_arrow)
                
                
    arrows.sort(key = lambda element:element.index)

    return user_input

def store_linkers_and_molecules(user_input, reaction_scheme, arrows):
    i = 0
    user_input_length = len(user_input)
    while i < user_input_length:
        current_char = user_input[i]
        if current_char in linker.linker_types or current_char == '@':
            user_input = user_input[:i] + '!' + user_input[i:]
            user_input = user_input[:i+2] + '!' + user_input[i+2:]
            i += 3
            user_input_length += 2
        else: i += 1

    
    print(user_input)
    user_input = user_input.strip('!')
    componenents = user_input.split("!")

    for component in componenents:
        if component in linker.linker_types:
           linker_to_append = linker(component)
           reaction_scheme.append(linker_to_append)
        elif component == '@':
            arrow_to_append = arrows[0]
            reaction_scheme.append(arrow_to_append)
            arrows.pop(0)
        else:
            if is_organic(component): 
                #Organic script or alternatively, 
                #send the name to the object, 
                #which processes the moleculer
                reaction_scheme.append(molecule(str(component), "organic", None))
            else:
                marked_character = ""
                atoms = []
                for character in component: 
                    
                    if character.isupper():
                        marked_character += "@" + character
                    else:
                        marked_character += character
                        atoms = marked_character.split("@")
                
                reaction_scheme.append(molecule(str(component), "inorganic", atoms))

    print(reaction_scheme)
    """


"""                      
def configure_input(user_input):
    occurrences = user_input.count("\"")
    if occurrences % 2 != 0:
        print("Invalid input!")
    elif occurrences != 0:
        indices = [0]
        current_index = -1
        configured_input = user_input[:]

        for _ in range(occurrences):
            current_index = user_input.index("\"")
            indices.append(current_index)
            user_input = user_input.replace("\"","!", 1)

        indices.append(len(user_input))

        for i in range(int(len(indices)/2)):
            sub_string = user_input[indices[2*i]:indices[2*i+1]]
            configured_input = user_input.replace(sub_string,sub_string.replace(" ","")) 
            
            
    else: user_input = user_input.replace(" ","")
    print(user_input)
    """    
#Processes input into a list of objects 
def get_input():
    arrows = []
    reaction_scheme = []

    user_input = str(input("enter a reaction")).replace("\\\"","@")
    if user_input.count("\"") % 2 != 0:
        print("invalid input")

    #configure_input(user_input)
    user_input = store_arrows(user_input, arrows)
    #store_linkers_and_molecules(user_input, reaction_scheme, arrows)
    
        

            
                


    """
    reagents = user_input.split(" ")

    for reagent in reagents:
        checked = False
        
        for potential_linker in linker.linker_types:
            if not checked and reagent == potential_linker:
                linker_to_append = linker(potential_linker)
                reaction_scheme.append(linker_to_append)
                checked = True
                break

        for potential_arrow in arrow.arrow_types:
            if not checked and reagent == potential_arrow: 
                arrow_to_append = arrow(potential_arrow)
                reaction_scheme.append(arrow_to_append)
                checked = True            
                break 
        
        if not checked:
            if is_organic(reagent): 
                #Organic script or alternatively, 
                #send the name to the object, 
                #which processes the moleculer
                reaction_scheme.append(molecule(str(reagent), "organic"))
                break
            else:
                marked_character = ""
                for character in reagent: 
                    if character.isupper():
                        marked_character += "@" + character
                    else:
                        marked_character += character
                        atoms = marked_character.split("@")
                        atoms.remove("")
                
                reaction_scheme.append(molecule(str(reagent), "inorganic", atoms))
    print(reaction_scheme)

"""
#Determines whether molecule is organic based on length-criteria
#Assumes input is given in symbolic form, i.e. CO_2 not carbondioxide

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

get_input()