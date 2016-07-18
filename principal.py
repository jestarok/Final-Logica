#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.chdir("C:\\Program Files (x86)\\swipl\\bin")
from pyswip import *
from Tkinter import *
import operator
master = Tk()
master.minsize(500,500)
prolog = Prolog()
prolog.consult("C:/Users/Public/prol/final.pl")
global mensajeSan, mensajeFla, mensajeCol,mensajeMela
mensajeSan = "Este temperamento está basado en un tipo de sistema nervioso rápido y equilibrado que se caracteriza por poseer una alta sensibilidad, "+\
             "un bajo nivel de actividad y fijación de la concentración y una moderada reactividad al medio; es característico "+\
             "del sistema nervioso una moderada correlación de la actividad a la reactividad; es extrovertido y manifiesta alta flexibilidad a los cambios de ambiente.\n\n"+\
             "Se trata de una persona cálida, campante, vivaz y que disfruta de la vida siempre que se pueda. Es receptiva por naturaleza, "+\
             "las impresiones externas encuentran fácil entrada en su interior en donde provocan un alud de respuestas. Tiende a tomar decisiones basándose "+\
             "en los sentimientos más que en la reflexión. Es tan comunicativo que es considerado un extrovertido. Tiene una capacidad insólita para disfrutar "+\
             "y por lo general contagia a los demás su espíritu que es amante de la diversión. Este tipo de personas por lo general, hablan antes de pensar, son extrovertidas, muy activas e intuitivas."

mensajeFle = "Basado en un tipo de sistema nervioso lento y equilibrado que se caracteriza por tener una baja sensibilidad pero una alta actividad y concentración de la atención; "+\
             "es característico de su sistema nervioso una baja reactividad a los estímulos del medio, y una lenta correlación de la actividad a la reactividad, es introvertido y posee baja flexibilidad a los cambios de ambiente. "+\
             "Es tranquilo, nunca pierde la compostura y casi nunca se enfada. Por su equilibrio, es el más agradable de todos los temperamentos. Trata de no involucrarse demasiado en las actividades de los demás."+\
             " Por lo general suele ser una persona apática, además de tener una buena elocuencia. No busca ser un líder, sin embargo puede llegar a ser uno muy capaz.\n\n"+\
             "Es un individuo calmado, tranquilo, que nunca se descompone y que tiene un punto de ebullición tan elevado que casi nunca se enfada. Son personas serias, impasibles y altamente racionales."+\
             " Son calculadores y analíticos. Generalmente, ese temperamento de personas muy capaces y equilibradas. Es el tipo de persona más fácil de tratar y es por esa naturaleza el más agradable de los temperamentos."+\
             " El flemático es frío y se toma su tiempo para la toma de decisiones. Prefiere vivir una existencia feliz, placentera y sin estridencias hasta el punto que llega a involucrarse en la vida lo menos que puede."

mensajeMela = "Basado en un tipo de sistema nervioso débil, posee una muy alta sensibilidad, un alto nivel de actividad y concentración de la atención, así como una baja reactividad ante los estímulos del medio, y una baja"+\
             " correlación de la actividad a la reactividad; es introvertido y lo caracteriza una baja flexibilidad a los cambios en el ambiente."+\
             "Es abnegado, perfeccionista y analítico. Es muy sensible emocionalmente. Es propenso a ser introvertido, sin embargo, puede actuar de forma extrovertida."+\
             " No se lanza a conocer gente, sino deja que la gente venga a él. Sus tendencias perfeccionistas y su conciencia hacen que sea muy fiable, pues no le permiten abandonar a alguien cuando están contando con él."+\
             " Además de todo, posee un gran carácter que le ayuda a terminar lo que comienza. Pero es difícil convencerlo de iniciar algún proyecto, debido a que siempre está considerando todos los pros y contras en cualquier situación.\n\n"+\
             " El melancólico es el más rico y complejo de todos los temperamentos. Suele producir tipos analíticos, abnegados, dotados y perfeccionistas. Es de una naturaleza emocional muy sensible, predispuesto a veces a la depresión."+\
             " Es el que consigue más disfrute de las artes. Es propenso a la introversión, pero debido al predominio de sus sentimientos, puede adquirir toda una variedad de talentos. Tiende a ser una persona pesimista. "+\
             "Tiene cambios emocionales muy bruscos, y se puede decir que se puede hacerlo enojar fácilmente. No le gusta que lo interrumpan cuando se concentra en algo que es importante para él. Se enamora con facilidad y lo hace muy seriamente."

mensajeCol = "Está basado en un tipo de sistema nervioso rápido y desequilibrado, posee alta sensibilidad y un nivel alto de actividad y concentración de la atención, aunque tiene alta reactividad a los estímulos del medio y una muy alta correlación, "+\
             "también es flexible a los cambios de ambiente. Cuando se le describe o dice algo que le fastidia o desagrada, trata de callar de forma violenta a las personas que se lo dicen. Es rápido, muy activo, práctico en sus decisiones, autosuficiente"+\
             " y sobre todo independiente. Es extrovertido, pero no tanto como la persona de temperamento sanguíneo. Se fija metas y objetivos. Es muy ambicioso. Valora rápida e intuitivamente y no reconoce los posibles tropiezos y obstáculos que puede "+\
             "encontrar en el camino si busca lograr una meta.\n\n Es caluroso, rápido, activo, práctico, voluntarioso, autosuficiente y muy independiente. Tiende a ser decidido y de firmes opiniones, tanto para sí mismo como para otras personas, y tiende a "+\
             "tratar de imponerlas. Es extrovertido, no hasta el punto del sanguíneo. Generalmente, prefiere la actividad. No necesita ser estimulado por su ambiente, sino que más bien lo estimula él con sus inacabables ideas, planes, metas. Tiende a "+\
             "fijarse metas muy altas, porque considera que es capaz, pero no siempre las cumple, no por falta de capacidad sino de tiempo o tropiezos encontrados. Dominante y hasta manipulador para alcanzar su objetivo. Tiende a ser manipulador, pero "+\
             "también es muy intolerante. Quiere hacer todo lo que desee."

def asertarMemoria():
    archivo = open("C:/Users/Public/prol/final.txt","r")
    for linea in archivo.readlines():
        lista = linea.split("_")
        dos = lista[2].split(".")
        list(prolog.query("assertz(personalidad(" + str(lista[0]) + str(lista[1]) + "," + str(dos[0]) + "))."))

    #for uno in prolog.query("personalidad(Nombre,Person)"):
       # print uno["Nombre"],uno["Person"]
    archivo.close()


asertarMemoria()

#Para el boton registro, Este nombre se utilizo para calmar el estres de trabajar desde el sabado hasta el Lunes a las 2AM
def juanLuigi():
    var= "grasa de atra"

#Para el boton relaciones
def relaciones():
    sii = "siiiiiii"

def registro():
    def inicio():
        if tfnombre.get() != "" and tfapellido.get() != "":
            Test(tfnombre.get().lower(), tfapellido.get())
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


def resultado(N, A, Max):
    # Manejo del archivo
    archivo = open("C:/Users/Public/prol/final.txt", "a+")
    archivo.write(N + "_" + A + "_" + str(Max) + ".\n")
    archivo.close()
    #ventana de resultados
    result = Toplevel()
    result.minsize(400,450)
    text = Text(result)
    text.insert(INSERT,N+" "+A+" tu personalidad es: "+ str(Max)+"\n\n")
    if Max == "sanguineo":
        text.insert(INSERT,mensajeSan)
    elif Max == "colerico":
        text.insert(INSERT, mensajeCol)
    elif Max == "flematico":
        text.insert(INSERT, mensajeFle)
    elif Max == "melancolico":
        text.insert(INSERT, mensajeMela)
    text.pack()
    text.tag_add("all", "1.0", "30.0")
    text.tag_config("all", font="Times 16", justify=CENTER)

    list(prolog.query("assertz(personalidad(" + str(N) + str(A) + "," + str(Max) + "))."))

    # Aqui se escribe el archivo con el nombre y el tipo de la persona
    # Se ensena quien hizo el test, que salio y que significa.
    # Se hace un assert para la opcion de quienes son los de ese tipo.


#Funciones y elaboracion del Test
def Test(N,A):
    nombre = StringVar()
    apellido = StringVar()
    nombre.set(N)
    apellido.set(A)
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
            contmelancolicas.set(contmelancolicas.get()+1)
        elif numero == 3:
            contflematicas.set(contflematicas.get()+1)


    def maxindex():
        list = [contsanguinea.get(),contcolericas.get(),contmelancolicas.get(),contflematicas.get()]
        index, value = max(enumerate(list), key=operator.itemgetter(1))
        print index
        if index == 0:
            return "sanguineo"
        elif index == 1:
            return "colerico"
        elif index == 2:
            return "melancolico"
        elif index == 3:
            return "flematico"


    def next(contador):
        if(contpregunta.get() == 14):
            test.destroy()
            resultado(nombre.get(),apellido.get(),maxindex())
        else:
            contpregunta.set(contpregunta.get()+1)
            preguntalbl.config(text=preguntas[contpregunta.get()])
            btn1.config(text=palabrassanguineas[contpregunta.get()])
            btn2.config(text=palabrascolericas[contpregunta.get()])
            btn3.config(text=palabrasmelancolicas[contpregunta.get()])
            btn4.config(text=palabrasflematicas[contpregunta.get()])
            sumarpuntos(contador)
            print contsanguinea.get(),contcolericas.get(),contmelancolicas.get(),contflematicas.get()

        # maxi.set(max(contsanguinea.get(),contcolericas.get(),contmelancolicas.get(),contflematicas.get()))


    for pregunta in prolog.query("pregunta(P)"):
        preguntas.append(pregunta["P"])

    for palabras in prolog.query("palabras('C:/Users/Public/prol/sanguineo.txt',PS)"):
        palabrassanguineas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/Users/Public/prol/colerico.txt',PS)"):
        palabrascolericas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/Users/Public/prol/melancolico.txt',PS)"):
        palabrasmelancolicas.append(palabras["PS"])
    for palabras in prolog.query("palabras('C:/Users/Public/prol/flematico.txt',PS)"):
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
test.add_command(label="Registro",command=juanLuigi)
test.add_command(label="Relaciones",command=relaciones)
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