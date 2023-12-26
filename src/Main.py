import sys 
import os

current_path = os.getcwd()
sys.path.insert(0,f'{current_path}\\objects')
from example import fib
print(fib(4))
