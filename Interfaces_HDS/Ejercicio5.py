# #ULTIMO EJERCICIO
# from tkinter import *
# ventana=Tk()
# ventana.geometry('270x500')

# Widget_uno=Frame()
# Widget_uno.grid(row=0,column=0)
# Widget_uno.config(width=30,height=30)

# Widget_uno=Frame()
# Widget_uno.grid(row=1,column=0)
# Widget_uno.config(width=30,height=30)

# Widget_uno=Frame()
# Widget_uno.grid(row=2,column=0)
# Widget_uno.config(width=30,height=30)

# Widget_dos=Frame()
# Widget_uno.config(width=50,height=50)
# Widget_dos.grid(row='3',column='0',columnspan='2')
# Widget_dos.config(width='200',height='100')
# Widget_dos.config(bg='red')
# #creacion de etiqueta
# etiqueta=Label(ventana,text='INGRRESA TU NOMBRE')
# etiqueta.grid(row=0,column=0)
# etiqueta=Label(ventana,text='DNI')
# etiqueta.grid(row=1,column=0)
# etiqueta=Label(ventana,text='CELULAR')
# etiqueta.grid(row=2,column=0)
# #creacion de cuadro
# cuadro_texto=Entry()
# cuadro_texto.grid(row=0,column=1)
# cuadro_texto=Entry()
# cuadro_texto.grid(row=1,column=1)
# cuadro_texto=Entry()
# cuadro_texto.grid(row=2,column=1)

# ventana.mainloop()

# from tkinter import *
# ventana=Tk()
# ventana.title("mi ventana")
# ventana.geometry("500x400")

# colum_izquierda=Frame()
# colum_izquierda.grid(row=0,column=0)
# colum_izquierda.config(Widget=200,height=5)
# etiqueta=Label(ventana,text="esta es mi etiqueta")
# etiqueta.grig(row=0,column=1)

# ventana.mainloop()

from tkinter import *
ventana=Tk()
ventana.geometry('270x500')

Widget_uno=Frame()
Widget_uno.grid(row=0,column=0)
Widget_uno.config(width=30,height=30)

Widget_uno=Frame()
Widget_uno.grid(row=1,column=0)
Widget_uno.config(width=30,height=30)

Widget_uno=Frame()
Widget_uno.grid(row=2,column=0)
Widget_uno.config(width=30,height=30)

Widget_uno=Frame()
Widget_uno.grid(row=3,column=0)
Widget_uno.config(width=30,height=30)

Widget_uno=Frame()
Widget_uno.grid(row=4,column=0)
Widget_uno.config(width=30,height=30)

etiqueta=Label(ventana,text='INGRRESA UN NUMERO')
etiqueta.grid(row=0,column=0)
etiqueta=Label(ventana,text='INGRESE OTRO NUMERO')
etiqueta.grid(row=1,column=0)
etiqueta=Label(ventana,text='RESULTADO')
etiqueta.grid(row=2,column=0)
etiqueta.grid(row=3,column=0)
etiqueta=Label(ventana,text='LIMPIAR')
etiqueta.grid(row=4,column=0)

cuadro_texto=Entry()
cuadro_texto.grid(row=0,column=1)
cuadro_texto=Entry()
cuadro_texto.grid(row=1,column=1)
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=1)
ventana.mainloop()