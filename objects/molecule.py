from functional_group import *

functional_groups = {
    "carboxylic acid":{"rep":"C(--O)O"},
    "ester":{"rep":"C(--O)O"},
    "amide":{"rep":"C(--O)N"},
    "carbonyl":{"rep":"C(--O)"},
    "alcohol":{"rep":"CO"},
    "thiol":{"rep":"S"},
    "amine":{"rep":"N"},
    "arene":{"rep":""},
    "ether":{"rep":"O"},
    "alkene":{"rep":"--C--"},
    "alkyne":{"rep":"---C---"},
    "fluorine group":{"rep":"F"},
    "chlorine group":{"rep":"C"},
    "bromine group":{"rep":"Br"},
    "iodine group":{"rep":"I"},
    "alkane":{"rep":"C"},
    "nitrile":{"rep":"---N"},
    "azide": {"rep":"N--N--N"},
    "nitro group": {"rep":"N(--O)O"}
    }
functional_group_indicators = {
    "oxo": "carbonyl",
    "hydroxy": "alcohol",
    "amino": "amine",
    "oxy": "ether", 
    "fluoro": "fluorine group",
    "chloro": "chlorine group",
    "bromo": "bromine group",
    "iodo": "iodine group",
    "yl": "alkyl",
    "enyl": "alkenyl",
    "phenyl": "arene",
    "cyano": "nitrile",
    "azido": "azide",
    "nitro": "nitro compound",
    "oic acid" : "carboxylic acid",
    "carbonic acid" : "carboxylic acid",
    "ate": "ester",
    "amide": "amide",
    "al": "carbonyl",
    "one": "carbonyl",
    "ol": "alcohol",
    "thiol": "thiol",
    "amine": "amine",
    "ether": "ether",
    "ene": "alkene",
    "yne": "alkyne",
    "ane": "alkane",
    "benzene": "arene",
    "nitrile": "nitrile",
    "cyclo": "cyclic"
}
numbering_prefixes_for_chains = {
    "meth":1,
    "eth": 2,
    "prop":3,
    "but": 4,
    "penta": 5, 
    "hexa": 6, 
    "hepta": 7, 
    "octa": 8,
    "nona": 9,
    "decane":10,
}
numbering_prefixes_for_groups = {
    "mono": 1,
    "hen": 1,
    "un": 1,
    "di": 2,
    "eth": 2,
    "do": 2,
    "tri": 3,
    "prop":3,
    "tetr": 4,
    "but": 4,
    "pent": 5, 
    "hex": 6, 
    "hept": 7, 
    "oct": 8,
    "non": 9,
    }
numbering_prefixes_for_chains_tens = {
    "deca": 10,
    "icos": 20, 
}
"""
functional_group_prefixes = {
    "oxo":"carbonyl",
    "hydroxy": "alcohol",
    "amino": "amine",
    "oxy": "ether", 
    "fluoro": "fluorine group",
    "chloro": "chlorine group",
    "bromo": "bromine group",
    "iodo": "iodine group",
    "yl": "alkyl",
    "enyl": "alkenyl",
    "phenyl": "arene",
    "cyano": "nitrile",
    "azido": "azide",
    "nitro": "nitro compound",
    "cyclo":"cyclic"

}
"""
"""
functional_group_suffixes = {
    "oic acid" : "carboxylic acid",
    "carbonic acid": "carboxylic acid",
    "ate": "ester",
    "amide": "amide",
    "al": "aldehyde",
    "one": "ketone",
    "ol": "alcohol",
    "thiol": "thiol",
    "amine": "amine",
    "ether": "ether",
    "ene": "alkene",
    "yne": "alkyne",
    "ane": "alkane",
    "benzene": "arene",
    "nitrile": "nitrile",
}
"""

class molecule:
    def __init__(self,formula):
        self.name = formula

    def process_molecule(self):
        name = self.name
        groups_in_molecule = []     
        split_name = name.split("-")
        print(f"SplitName:{split_name}")
        positions = []
        for sub_string_index, sub_string in enumerate(split_name):
            is_number = False

            for char in sub_string:
                if char.isnumeric():
                    positions.append(int(char))
                elif sub_string == ",":
                    break

            for indicator in list(functional_group_indicators):
                if indicator in sub_string:
                    if len(positions) == 0:
                        positions.append(1)
    
                    if indicator == "yl":
                        for alkyl_prefix in numbering_prefixes_for_chains:
                            if alkyl_prefix + indicator in sub_string:
                                #groups_in_molecule.append(functional_group(functional_group_indicators[alkyl_prefix+indicator], positions, ""))
                                positions = [] 
                    elif "cyclo" in sub_string:
                        groups_in_molecule.append(functional_group(functional_group_indicators[indicator], positions, sub_string))
                        positions = []  
                    else: 
                        groups_in_molecule.append(functional_group(functional_group_indicators[indicator], positions, ""))
                        positions = [] 
                                     
                for potential_longest_chain in numbering_prefixes_for_chains:
                    if potential_longest_chain in sub_string:                            
                        longest_chain = numbering_prefixes_for_chains[potential_longest_chain]
                        break

        for n in groups_in_molecule:
            print(f"There is a(n) {n.group_type} at carbon(s) number {n.positions}")
        
        print(f"The longest chain is {longest_chain} carbons long")
        
        return groups_in_molecule

my_molecule = molecule("2,2-dichloro-4-cyclobutylbutanoic acid")
my_molecule.process_molecule()

