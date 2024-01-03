#Get's the period of an element, given it's atomic number
"""
def get_period(atomic_number):
        period = 0 
        while atomic_number > 0:
            period += 1
            atomic_number -= 2*period**2
        
        return period
"""
a = "Hello World!"
print(a[0:len(a)-1])