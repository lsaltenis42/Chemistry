from dataclasses import replace
import os
import sys
#from unittest.util import unorderable_list_difference

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
                second_quotation_mark_index = arrow_start_index - 1 - get_best_match(sub_string) - 1 #Used to say: second_quotation_mark_index = arrow_start_index - 1 - sub_string.index("\"") - 1
                before_caption = user_input[second_quotation_mark_index:arrow_start_index] #Double quotation marks in results can be fixed by adding and subtracting 1
                arrow_start_index = second_quotation_mark_index

            if arrow_end_index < len(user_input) -1 and user_input[arrow_end_index+1] == "\"": #Checks if caption exists after arrow
                sub_string = user_input[arrow_end_index+2:]
                second_quotation_mark_index = arrow_end_index+2 + sub_string.index("\"")
                after_caption = user_input[arrow_end_index+1:second_quotation_mark_index+1]
                arrow_end_index = second_quotation_mark_index

            arrow_to_append = arrow(potential_arrow["style"], arrow_start_index, before_caption, after_caption)
            arrows.append(arrow_to_append)
            configured_substring = user_input[arrow_start_index:arrow_end_index].replace(user_input[arrow_start_index:arrow_end_index],"$")#Why not just "$"?
            user_input = user_input[:arrow_start_index] + configured_substring + user_input[arrow_end_index+1:]
    
    #What does this do?
    for i, item in enumerate(arrows):
        for j in arrows:
            caption_range = j.caption_index_range()
            if (item.index > caption_range["before"]["start_index"] and item.index < caption_range["before"]["end_index"]) or (item.index > caption_range["after"]["start_index"] and item.index < caption_range["after"]["end_index"]):
                arrows.pop(i)
    
    for arrow_number, itterated_arrow in enumerate(arrows):
        print("\n________________________________")
        print(f"Arrow_number:{arrow_number}")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print(f"|Arrow type:{itterated_arrow.type}\n|Index:{itterated_arrow.index}\n|Before caption:{itterated_arrow.caption["before"]}\n|After caption:{itterated_arrow.caption["after"]}")
    
    print(user_input)
    return user_input

"""
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

    user_input = str(input("enter a reaction")).replace(" ","")
    
    if user_input.count("\"") % 2 != 0:
        print("invalid input")

    #configure_input(user_input)
    user_input = store_arrows(user_input, arrows)
    #store_linkers_and_molecules(user_input, reaction_scheme, arrows)
    
#Finds the most likely end quotation mark by scanning for a second arrow, 
#and preferably choosing the last available quotation mark.
#Still needs to be implemented for captions after the arrow.
def get_best_match(sub_string):
    best_match = sub_string.index("\"")

    if sub_string.count("\"") > 1:
        furthest_arrow_index = len(sub_string)-1
        for potential_reverse_arrow in arrow.arrow_types:
            reversed_arrow = potential_reverse_arrow["style"][::-1]
            if reversed_arrow in sub_string:
                if sub_string.index(reversed_arrow) < furthest_arrow_index:
                    furthest_arrow_index= sub_string.index(reversed_arrow)            
    
        list_of_quotation_indexes = []
        for char_index, char in enumerate(sub_string):
            if char == "\"": 
                list_of_quotation_indexes.append(char_index)

        smallest_difference = len(sub_string) - 1 
                    
        for index in list_of_quotation_indexes:
            if abs(index - furthest_arrow_index) < smallest_difference:
                smallest_difference = abs(index - furthest_arrow_index)
                best_match = index
    print(best_match)
    return int(best_match)

#Determines whether molecule is organic based on length-criteria
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