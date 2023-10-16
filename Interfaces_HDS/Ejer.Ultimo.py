#ULTIMO EJERCICIO
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

Widget_dos=Frame()
Widget_uno.config(width=50,height=50)
Widget_dos.grid(row='3',column='0',columnspan='2')
Widget_dos.config(width='200',height='100')
Widget_dos.config(bg='red')
#creacion de etiqueta
etiqueta=Label(ventana,text='INGRRESA TU NOMBRE')
etiqueta.grid(row=0,column=0)
etiqueta=Label(ventana,text='DNI')
etiqueta.grid(row=1,column=0)
etiqueta=Label(ventana,text='CELULAR')
etiqueta.grid(row=2,column=0)
#creacion de cuadro
cuadro_texto=Entry()
cuadro_texto.grid(row=0,column=1)
cuadro_texto=Entry()
cuadro_texto.grid(row=1,column=1)
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=1)

ventana.mainloop()
