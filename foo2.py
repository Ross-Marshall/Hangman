#!/usr/bin/python
import sys
sys.path.append('/me/code/python/hangman/Imaging-1.1.7')
sys.path.append('/me/code/python/hangman/Imaging-1.1.7/PIL')

#import Tkinter
#from PIL import ImageTk, Image

import Tkinter as tk

def gamescreen():    
    photo = PhotoImage(file="img1.gif")
    canvas.bind("<Button-1>", buttonclick_gamescreen)
    canvas.pack(expand = YES, fill = BOTH)
    canvas.create_image(1, 1, image = photo, anchor = NW)
    game1 = PhotoImage(file="1.gif")
    canvas.create_image(30, 65, image = game1, anchor = NW)
    e1 = Entry(canvas)
    e2 = Entry(canvas)
    canvas.create_window(window = e1, x=10, y=10)
    canvas.create_window(window = e2 , x=400, y=10)    
    canvas.update()
    window.mainloop()

gamescreen()
