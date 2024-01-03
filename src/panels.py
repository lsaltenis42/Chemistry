import os
import sys
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Window")
window_width = int(window.winfo_screenwidth()*75/100)
window_height = int(window.winfo_screenheight()*90/100)
window.geometry(f"{window_width}x{window_height}")

print(window_width)

standard_settings = {"bond_length" : 10,
                       "atom_size" : 5 
                    }

def create_input_panel():
    panel_frame_width = int(window_width*30/100)
    panel_frame_height = int(window_height*30/100)
    panel_frame = Frame(window, width= panel_frame_width, height= panel_frame_height)
    panel_frame.grid(column = 0, row = 0, rowspan = 3, ipadx= 0, ipady= 0)
    
    rules_label = Label(panel_frame,text = f"Enter reactionscheme \n using IUPAC nomenclature", width= 20, height=2)
    rules_label.grid(column = 0, row = 0)

    entry_box = Entry(panel_frame, width= int(panel_frame_width/16))
    entry_box.grid(column = 0, row = 1)

    structure_button = Button(panel_frame, text = "Generate structure", command = draw_reactionscheme, width= 16, height=1)
    structure_button.grid(column = 0, row = 2)

def create_settings_panel():
    panel_frame_width = int(window_width*30/100)
    panel_frame_height = int(window_height*70/100)
    panel_frame = Frame(window, height=panel_frame_height, width=panel_frame_width)
    panel_frame.grid(column = 0, row = 3, pady=0)
    print(panel_frame_width)

    settings_panel = ttk.Notebook(panel_frame, height = panel_frame_height, width = int(panel_frame_width/16))
    settings_panel.grid(column = 0, row = 4)

    display_settings = ttk.Frame(settings_panel)   
    export_settings = ttk.Frame(settings_panel)   
    settings_panel.add(display_settings, text='Display')
    settings_panel.add(export_settings, text='Export')

def draw_bond(start_atom, end_atom):
    """"""

def draw_atom(atom):
    """"""

def draw_reactionscheme():
    #Coordinates originate in the top left corner with x increasing to the right, and y increasing down.
    canvas_width = int(window_width*75/100)
    canvas_height= int(window_height*87/100)
    canvas = Canvas(window, width=canvas_width, height=canvas_height, background='white')
    canvas.grid(column=1, row=0, rowspan= 10)

    initial_x = canvas_width/20
    initial_y = canvas_height/2

    canvas.create_line(10, 10, 200, 50, fill='red', width=3)


    
create_settings_panel()
create_input_panel()

window.mainloop()


