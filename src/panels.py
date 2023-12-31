import os
import sys
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Window")
window_width = int(window.winfo_screenwidth()*75/100)
window_height = int(window.winfo_screenheight()*90/100)
window.geometry(f"{window_width}x{window_height}")

standard_settings = {"bond_length" : 10,
                       "atom_size" : 5
                    }

def create_input_panel():
    panel_frame_width = int(window_width*30/100)
    panel_frame_height = int(window_height*30/100)
    panel_frame = Frame(window, width= panel_frame_width, height= panel_frame_height, bg="red")
    panel_frame.grid(column = 0, row = 0, rowspan = 3)
    
    rules_label = Label(panel_frame,text = f"Enter reactionscheme \n using IUPAC nomenclature")
    rules_label.grid(column = 0, row = 0)

    entry_box = Entry(panel_frame, width= 10)
    entry_box.grid(column = 0, row = 1)

    structure_button = Button(panel_frame, text = "Generate structure", command = draw_reactionscheme)
    structure_button.grid(column = 0, row = 2)

def create_settings_panel():
    panel_frame = Frame(window)
    panel_frame.grid(column = 0, row = 3)

    settings_panel = ttk.Notebook(panel_frame, height = 200, width = 100)
    settings_panel.grid(column = 0, row = 4)

    display_settings = ttk.Frame(settings_panel)   
    export_settings = ttk.Frame(settings_panel)   
    settings_panel.add(display_settings, text='Display')
    settings_panel.add(export_settings, text='Export')

def draw_bond(start_atom, end_atom):
    """"""

def draw_reactionscheme():
    canvas_width = window_width*70/100
    canvas_height= window_height
    canvas = Canvas(window, width=canvas_width, height=canvas_height, background='white')
    canvas.grid(column=1, row=0, rowspan= 10)
    
create_settings_panel()
create_input_panel()

window.mainloop()


