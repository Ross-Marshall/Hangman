from numpy import *
import matplotlib.pyplot as plt
fromTkinter import *
import tkMessageBox
from pylab import savefig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
import matplotlib.backend_bases       
from matplotlib.figure import Figure

def rutherford():
    tkMessageBox.showinfo("hello world", j)
def N():
    tkMessageBox.showinfo("Variable N", "Number of alpha particles incident on foil")

def T():
    tkMessageBox.showinfo('Variable t', 'Thickness of foil in metres')

def K():
    tkMessageBox.showinfo('Variable E', 'Kinetic energy of alpha particles in joules')

def atom():
    tkMessageBox.showinfo('Variable Z', 'Atomic number of element from which the foil is made, or the name of the element')



class App:
    def __init__(self, master):
        frame = Frame(master) #creates the first frame

        Button(frame, text = "?", command=N).grid(row=1,column=2) #various help buttons
        Button(frame, text = "?", command=T).grid(row=2,column=2)
        Button(frame, text = "?", command=K).grid(row=3,column=2)
        Button(frame, text = "?", command=atom).grid(row=4,column=2)

        Nlabel = Label(frame, text = "N =").grid(row=1, column=0, sticky=E) #labels next to the entry frame
        tlabel = Label(frame, text="t =").grid(row=2,column=0, sticky=E)    
        Elabel = Label(frame, text="E =").grid(row=3,column=0, sticky=E)        
        Zlabel = Label(frame, text="Z =").grid(row=4, column=0, sticky=E)

        eN=Entry(frame)
        eN.grid(row=1,column=1)
        et=Entry(frame)
        et.grid(row=2,column=1)
        eE=Entry(frame)
        eE.grid(row=3,column=1)
        eZ=Entry(frame)
        eZ.grid(row=4,column=1)

        def flup():         #the plot
            N=float(eN.get())#turn string into float
            t=float(et.get())
            E=float(eE.get())
            Z=float(eZ.get())
            r=10*(10**-10)
            e=1.602*(10**-19)
            a=5*(10**30)
            i = linspace(math.pi/80, math.pi, 1000)
            list =[]

            for p in i:
                b = (N*a*t)/(16.0*(r**2))
                c = ((2.0*Z*(e**2))/(E*4.0*math.pi*8.854*(10**-12)))**2
                d = (1.0/(math.sin(p/2.0)))**4
                n=b*c*d
                list.append(n)

            f=Figure(figsize=(5,4), dpi=100)
            g=f.add_subplot(1,1,1)


            g.plot(i,list)

            canvas=FigureCanvasTkAgg(f, master=master)
            canvas.show()
            canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)

            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


        #def clear():


        bgra=Button(frame, text = "Plot", command=flup) #this button makes the plot
        bgra.grid(row=5,column=1)

        delete=Button(frame,text='Clear All', command=clear)
        delete.grid(row=5,column=2)




        frame2=Frame(master)

        b1=Button(frame2, text="Rutherford Scattering??", command=rutherford)
        b1.pack(side=LEFT)
        frame2.pack()
        frame.pack()



root = Tk()
app = App(root)
root.mainloop()
