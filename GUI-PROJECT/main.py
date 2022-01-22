from tkinter import *
from tkinter import ttk
'''nxt line create tk class that initialize tk and create assoiciated tcl interpretor, 
creates root window
'''
root = Tk()
'''creates a fram widget that contain label and button'''
Pad=10
borderwidth=0
frm = ttk.Frame(root, padding=Pad,borderwidth=borderwidth) 
# print(frm.configure())
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()