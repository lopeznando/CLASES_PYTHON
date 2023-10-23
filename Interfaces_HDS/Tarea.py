from tkinter import *

ventana=Tk()

num_uno=Label(ventana,text="Ingrese las notas")
num_uno.grid(row=0,column=0)
text_uno=Entry()
text_uno.grid(row=0,column=1)

rpt=Label(ventana,text="PROMEDIO")
rpt.grid(row=2,column=0)
rpt_text=Entry()
rpt_text.grid(row=2,column=1)

def promedio():
		n1=int(text_uno.get())
		resultado=n1//5
		rpt_text.insert(0,resultado)
		
boton_sum=Button(ventana,text="PROMEDIO",command=promedio).grid(row=3,column=0)

def limpiar():
		text_uno.delete(0,END)
		rpt_text.delete(0,END)
		text_uno.focus()

boton_limpiar=Button(ventana,text="LIMPIAR", command=limpiar).grid(row=3,column=1)
		
ventana.mainloop()

