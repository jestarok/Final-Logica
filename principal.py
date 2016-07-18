import os
os.chdir("C:\\Program Files (x86)\\swipl\\bin")
from pyswip import *
from Tkinter import *
import operator
master = Tk()
master.minsize(500,500)
prolog = Prolog()
prolog.consult("C:/prol/final.pl")


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
    contsanguinea = IntVar()
    contsanguinea.set(0)
    contcolericas =IntVar()
    contcolericas.set(0)
    contmelancolicas = IntVar()
    contmelancolicas.set(0)
    contflematicas = IntVar()
    contflematicas.set(0)
    palabrassanguineas = []
    palabrasmelancolicas = []
    palabrascolericas = []
    palabrasflematicas = []
    preguntas = []

    def sumarpuntos(numero):
        print numero
        if numero == 0:
            contsanguinea.set(contsanguinea.get()+1)
        elif numero == 1:
            contcolericas.set(contcolericas.get()+1)
        elif numero == 2:
            contmelancolicas.set(contmelancolicas.get() +1)
        elif numero == 2:
            contflematicas.set(contflematicas.get()+1)

    def maxindex():
        list = [contsanguinea.get(),contcolericas.get(),contmelancolicas.get(),contflematicas.get()]
        index, value = max(enumerate(list), key=operator.itemgetter(1))
        if index == 0:
            return "sanguineo"
        elif index == 1:
            return "colerico"
        elif index == 2:
            return "melancolico"
        elif index == 2:
            return "flematico"

    def next(contador):
        if(contpregunta.get() == 14):
            print maxindex()
            test.destroy()
        else:
            contpregunta.set(contpregunta.get()+1)
            preguntalbl.config(text=preguntas[contpregunta.get()])
            btn1.config(text=palabrassanguineas[contpregunta.get()])
            btn2.config(text=palabrascolericas[contpregunta.get()])
            btn3.config(text=palabrasmelancolicas[contpregunta.get()])
            btn4.config(text=palabrasflematicas[contpregunta.get()])
            sumarpuntos(contador)
            print contsanguinea.get(),contcolericas.get(),contmelancolicas.get(),contflematicas.get()

#        maxi.set(max(contsanguinea.get(),contcolericas.get(),contmelancolicas.get(),contflematicas.get()))


    for pregunta in prolog.query("pregunta(P)"):
        preguntas.append(pregunta["P"])

    for palabras in prolog.query("palabras('C:/prol/sanguineo.txt',PS)"):
        palabrassanguineas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/prol/colerico.txt',PS)"):
        palabrascolericas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/prol/melancolico.txt',PS)"):
        palabrasmelancolicas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/prol/flematico.txt',PS)"):
        palabrasflematicas.append(palabras["PS"])

    preguntalbl = Label(test, text=preguntas[contpregunta.get()])
    preguntalbl.pack()
    btn1 = Button(test,text=palabrassanguineas[contpregunta.get()],command=lambda: next(0))
    btn1.pack(side=LEFT,padx=25)
    btn2 = Button(test,text=palabrascolericas[contpregunta.get()],command=lambda: next(1))
    btn2.pack(side=LEFT,padx=25)
    btn3 = Button(test,text=palabrasmelancolicas[contpregunta.get()],command=lambda: next(2))
    btn3.pack(side=LEFT,padx=25)
    btn4 = Button(test,text=palabrasflematicas[contpregunta.get()],command=lambda: next(3))
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