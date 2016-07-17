import os
os.chdir("C:\\Program Files (x86)\\swipl\\bin")
from pyswip import *
from Tkinter import *

master = Tk()
master.minsize(500,500)
prolog = Prolog()
prolog.consult("C:/final.pl")

w = Label(master, text="FINAL")
w.pack()

def Test():



b1 = Button(master,text="Tomar Test", command = Test)
b2 = Button(master,text="Masa de Planetas")
b3 = Button(master, text="Tiempo respecto al Sol")

b3.pack()
b2.pack()
b1.pack()

b3.place(relx=.35, rely=.53)
b2.place(relx=.39,rely=.46)
b1.place(relx=.39,rely=.39)

mainloop()