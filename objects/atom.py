import periodictable 

#element = periodictable.elements[4]

class element:
    def get_valence_electrons():
        return 
    
    def get_space_in_shell(shell_number):
        return 2*shell_number**2
    
    def get_space_in_subshell(sub_shell):
        if sub_shell == "s":
            return 2
        elif sub_shell == "p":
            return 6
        elif sub_shell == "d":
            return 10
        elif sub_shell == "f":
            return 14
        
    def get_period(atomic_number):
        period = 0 
        while atomic_number > 0:
            period += 1
            atomic_number -= 2*period**2
        
        return period

        

class atom(element):
    def __init__(self,atomic_number,index):
        self.name = atomic_number
        self.index = index
    


