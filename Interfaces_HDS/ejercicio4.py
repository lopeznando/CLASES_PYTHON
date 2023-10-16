from tkinter import *
ventana=Tk()
ventana.geometry('400x500')
Widget_uno=Frame()
Widget_uno.grid(row=0,column=0)
Widget_uno.config(width=400,height=500)
Widget_uno.config(bg='red')
etiqueta=Label(ventana,text='hola soy una etiqueta')
etiqueta.grid(row=0,column=0)
ventana.mainloop()

from tkinter import *
ventana=Tk()
ventana.geometry('400x500')
Widget_uno=Frame()
Widget_uno.grid(row=0,column=0)
#config es para darle iun tamaño
Widget_uno.config(width=400,height=50)
#label para crear una etiqueta
etiqueta=Label(ventana,text='ingresa tu nombre')
etiqueta.grid(row=0,column=0)
#creacion de cuadros
cuadro_texto=Entry()
#grid es para ubicar la fila y columna
cuadro_texto.grid(row=2,column=0)
ventana.mainloop()


