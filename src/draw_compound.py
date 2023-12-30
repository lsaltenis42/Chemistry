import os
import sys
from tkinter import *
from tkinter import ttk

#Makes contents of objects file accessible
current_path = os.getcwd()
sys.path.insert(0,f'{current_path}//objects')

#Creates window 
window = Tk()
width, heigth = 500, 500
widget_width, widget_height = 0, 0
window.title("Window")
window.geometry(f"{width}x{heigth}")

def create_canvas():
    canvas = Canvas(window, width=500, height=400, background='white')
    canvas.grid(column=0, row=3)

def create_settings_panel():
    standard_settings = {"bond_length" : 10,
                         "atom_size" : 5
                         }
    
    setting_panel = Frame(window)
    setting_panel.grid(column = 1, row = 0)

    option = Label(setting_panel, text = "This is inside a frame")
    option.grid(column = 0, row = 0)

    options = Menu(setting_panel) 
    options.grid(column = 0, row = 1)

def generating_button_clicked():
    """"""

def draw_bond(start_atom, end_atom):
    """"""

rules_label = Label(window,text = "Enter reactionscheme \n Use IUPAC nomenclature")
rules_label.grid(column = 0, row = 0, padx = widget_width, pady = widget_height)

entry_box = Entry(window)
entry_box.grid(column = 0, row = 1, pady = widget_height)

generating_button = Button(window, text = "Generate structure", command = generating_button_clicked)
generating_button.grid(column = 0, row = 2, padx = widget_width, pady = widget_height)

create_canvas()

window.mainloop()