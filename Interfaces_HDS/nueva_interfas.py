#1. import tkinter: libreria para la creacion de interfaces grafica
from tkinter import *
#la libreria tkinter tiene tres grandes clases para la creacion de interfaces 
# Tk() el mas usado
# Tkk()
# Tcl()
#2. instanciar Tk() como generador de interfaz grafica
nueva_ventana=Tk()
#3. frame es tambien una clase frame() para crear una frame tengo que primero instanciarlo
menu_principal=Frame
#montamos o inicializamos el frame
menu_principal.pack()
#haciendo uso del metodo config le damos un tamoño
menu_principal.config(width='200',height='200')
#haciendo uso del metodo config le asignamos el color
menu_principal.config(bg='red')
#metodo de Tk() que mantiene la ejecucion de un programa en un bucle
nueva_ventana.mainloop()