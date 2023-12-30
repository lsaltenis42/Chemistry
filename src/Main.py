import sys 
import os
import user_input
from tkinter import *
from tkinter import ttk

current_path = os.getcwd()
sys.path.insert(0,f'{current_path}//objects')
user_input.get_input()



