functional_groups = {
    "carboxylic acid":{"rep":"C(--O)O"},
    "ester":{"rep":"C(--O)O"},
    "amide":{"rep":"C(--O)N"},
    "aldehyde":{"rep":"C(--O)"},
    "ketone":{"rep":"C(--O)"},
    "alcohol":{"rep":"CO"},
    "thiol":{"rep":"S"},
    "amine":{"rep":"N"},
    "arene":{"rep":"\cyclic(3*(C--C)))"},
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
functional_group_prefixes = {
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
    "nitro": "nitro compound"
}
functional_group_suffixes = {
    "oic acid" : "carboxylic acid",
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
longest_chain_prefixes = {
    "meth": 1, 
    "eth": 2,
    "prop": 3,
    "but": 4
}
numbering_prefixes_single_digit = {
    "mono": 1,
    "hen": 1,
    "un": 1,
    "di": 2,
    "do": 2,
    "tri": 3,
    "tetra": 4,
    "penta": 5, 
    "hexa": 6, 
    "hepta": 7, 
    "octa": 8,
    "nona": 9,
    }
numbering_prefixes_tens = {
    "deca": 10,
    "icos": 20, 
}

#Each subsequent increase by ten is formated as numbering_prefixes_single_digit + acontane

class functional_group:
    def __init__(self, species, location):
        self.species = species
        self.location = location

class molecule:
    def __init__(self,formula,type):
        self.name = formula
        self.type = type
     
    def convert_to_smiles(self):
        name = self.name
        converted_molecule = ""
        current_main_group = ""
        substring = ""
        longest_chain = 0

        for char_index, char in enumerate(name):
            """"""

            



        return converted_molecule





