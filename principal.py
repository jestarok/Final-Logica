import os
os.chdir("C:\\Program Files (x86)\\swipl\\bin")
from pyswip import *
from Tkinter import *

master = Tk()
master.minsize(500,500)
prolog = Prolog()
prolog.consult("C:/final.pl")


#Funciones y elaboracion del Test
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

#Mensaje de ayuda
def Ayuda():
    cuadroAyuda= Toplevel()
    cuadroAyuda.minsize(300,300)

#Pantalla principal
#menu
menu = Menu(master)
#boton Test
test = Menu(menu,tearoff=0)
test.add_command(label="Tomar Test",command= Test)
menu.add_cascade(label="Test",menu = test)

#boton Ayuda
ayuda = Menu(menu,tearoff=0)
ayuda.add_command(label="Ayuda",command= Ayuda)
menu.add_cascade(label="Help",menu=ayuda)

#Testo descriptivo de la aplicacion
text = Text(master)
text.insert(INSERT,"Esta aplicacion es un Test de personalidad especifico, en el cual, " +
                   "a traves de un conjunto de\n preguntas se determinara la tendencia " +
                   "hacia una de las cuatro(4) personalidades existentes, las\n cuales son:" +
                   " Colerico, Melancolico, Flematico, Sanguineo. \n\n Dentro de esta aplicacion"+
                   " se tiene las opciones de tomar el Test, luego de haberlo tomado: se\n puede obtener su tipo de "+
                   "pesonalidad, saber con quien tiende a llevarse mejor a traves de sus\n personalidades.")
text.pack()
text.tag_add("all","1.0","10.0")
text.tag_config("all",font="Times 16",justify=CENTER)

master.config(menu = menu)


mainloop()