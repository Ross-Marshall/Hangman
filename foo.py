#from tkinter import *
#from tkinter.ttk import *
import Image
sys.path.append('/me/code/python/hangman/Imaging-1.1.7/PIL')
import ImageTk


root = Tk()

myButton = Button(root)
myImage = PhotoImage(file='img1.gif')
myButton.image = myImage
myButton.configure(image=myImage)

root.mainloop()
