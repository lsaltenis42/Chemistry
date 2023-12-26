import tkinter as tk
window = tk.Tk()
window.title("Window")
width = 800
heigth = 800

window.geometry(f"{width}x{heigth}")

e = tk.Entry(window).anchor("center")
e = tk.Entry(window).location(width/2, heigth/2)


window.mainloop()