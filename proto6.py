#!/usr/bin/python
import sys
sys.path.append('/me/code/python/hangman/Imaging-1.1.7')
sys.path.append('/me/code/python/hangman/Imaging-1.1.7/PIL')

#import Tkinter
#from PIL import ImageTk, Image

import Tkinter as tk

def txtInput(text):
    pass

root = tk.Tk()
root.title("Hangman")
photo = tk.PhotoImage(file= r"/me/code/python/hangman/img1.gif")
#cv = tk.Canvas()
cv = tk.Canvas(root,width=664, height=642)
cv.pack(side='top', fill='both', expand='yes')
picture_x = 10
picture_y = 10
cv.create_image(picture_x, picture_y, image=photo, anchor='nw')
#cv.create_image(641, 400, image=photo, anchor='nw')

#e1 = Entry(cv)
#cv.create_window(window=e1, x=picture_x, y=picture_y+400+10)

x = 40
y = picture_y+400+20
cv.create_text(x, y, text='Enter Letter: ')

e1 = tk.Entry(cv)
x = 180
cv.create_window(x, y, window=e1)

x = 40
y = picture_y+400+50
cv.create_text(x, y, text='Word: ')

e1 = tk.Entry(cv)
x = 180
cv.create_text(x, y, text='H_NGM_N W__D')

x = 40
y = picture_y+400+80
cv.create_text(x, y, text='Guess List: ')

e1 = tk.Entry(cv)
x = 180
cv.create_text(x, y, text='[A,B,D,Z,Y,Q]')

x = 40
y = picture_y+400+110
button1 = tk.Button(cv, text = "Submit")
cv.create_window(x, y, window=button1)

cv.update()

root.mainloop()
