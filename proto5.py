#!/usr/bin/python
import sys
sys.path.append('/me/code/python/hangman/Imaging-1.1.7')
sys.path.append('/me/code/python/hangman/Imaging-1.1.7/PIL')

import Tkinter
from PIL import ImageTk, Image


class image_manip(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)

        self.ImbImage = Tkinter.Canvas(self)
        self.ImbImage.pack()

        i = ImageTk.PhotoImage(Image.open('test.png'))
        self.ImbImage.create_image(0, 0, image=i)

def run():
    image_manip(None).mainloop()
if __name__ == "__main__":
    run()
