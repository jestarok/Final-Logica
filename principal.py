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
    master = Toplevel()

    contpregunta = IntVar()
    contpregunta.set(0)
    palabrassanguineas = []
    palabrasmelancolicas = []
    palabrascolericas = []
    palabrasflematicas = []
    preguntas = []

    def next():
        contpregunta.set(contpregunta.get()+1)
        preguntalbl.config(text=contpregunta.get())

    for pregunta in prolog.query("pregunta(P)"):
        preguntas.append(pregunta["P"])

    for palabras in prolog.query("palabras('C:/sanguineo.txt',PS)"):
        palabrassanguineas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/colerico.txt',PS)"):
        palabrascolericas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/melancolico.txt',PS)"):
        palabrasmelancolicas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/flematico.txt',PS)"):
        palabrasflematicas.append(palabras["PS"])

    preguntalbl = Label(master, text=contpregunta.get())
    preguntalbl.pack()
    btn = Button(master,text="wii",command=lambda: next())
    btn.pack()
    preguntalbl.update_idletasks()

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