import os
os.chdir("C:\\Program Files (x86)\\swipl\\bin")
from pyswip import *
from Tkinter import *

master = Tk()
master.minsize(500,500)
prolog = Prolog()
prolog.consult("C:/final.pl")


def registro():
    def inicio():
        if tfnombre.get() != "" and tfapellido.get() != "":
            Test(tfnombre.get(), tfapellido.get())
            register.destroy()

    register = Toplevel()
    register.minsize(150,150)
    lblnombre = Label(register,text="Nombre: ")
    tfnombre = Entry(register)
    lblapellido = Label(register, text="Apellido: ")
    tfapellido = Entry(register)
    start = Button(register,text="Iniciar Test",command=inicio)
    lblnombre.pack()
    tfnombre.pack()
    lblapellido.pack()
    tfapellido.pack()
    start.pack(side=BOTTOM)


#Funciones y elaboracion del Test
def Test(H,P):
    print H,P
    test = Toplevel()
    test.minsize(600,255)
    contpregunta = IntVar()
    contpregunta.set(0)
    contsanguinea = 0
    contcolericas = 0
    contmelancolicas = 0
    contflematicas = 0
    palabrassanguineas = []
    palabrasmelancolicas = []
    palabrascolericas = []
    palabrasflematicas = []
    preguntas = []

    def next():
        if(contpregunta.get() == 14):
            #resultado()
            test.destroy()
        else:
            contpregunta.set(contpregunta.get()+1)
            preguntalbl.config(text=preguntas[contpregunta.get()])
            btn1.config(text=palabrassanguineas[contpregunta.get()])
            btn2.config(text=palabrascolericas[contpregunta.get()])
            btn3.config(text=palabrasmelancolicas[contpregunta.get()])
            btn4.config(text=palabrasflematicas[contpregunta.get()])




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

    preguntalbl = Label(test, text=preguntas[contpregunta.get()])
    preguntalbl.pack()
    btn1 = Button(test,text=palabrassanguineas[contpregunta.get()],command=lambda: next())
    btn1.pack(side=LEFT,padx=25)
    btn2 = Button(test,text=palabrascolericas[contpregunta.get()],command=lambda: next())
    btn2.pack(side=LEFT,padx=25)
    btn3 = Button(test,text=palabrasmelancolicas[contpregunta.get()],command=lambda: next())
    btn3.pack(side=LEFT,padx=25)
    btn4 = Button(test,text=palabrasflematicas[contpregunta.get()],command=lambda: next())
    btn4.pack(side=LEFT,padx=25)
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
test.add_command(label="Tomar Test",command= registro)
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