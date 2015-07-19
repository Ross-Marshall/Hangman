#!/usr/bin/python

import Tkinter
import tkMessageBox
from Tkinter import *

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="green", height=800, width=800)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

T = Text( top, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")

C.pack()

Label(top, text="First Name").grid(row=0)
Label(top, text="Last Name").grid(row=1)

e1 = Entry(top)
e2 = Entry(top)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#Button(top, text='Quit', command=top.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(top, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

top.mainloop()
