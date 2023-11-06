

from tkinter import *

ventana = Tk()
ventana.geometry('300x300')

etiqueta = Label(ventana, text='Ingresa un número')
etiqueta.grid(row=0, column=0)

numero1 = Entry(ventana)
numero1.grid(row=1, column=0)  

etiqueta = Label(ventana, text='Ingresa otro número')  
etiqueta.grid(row=2, column=0)

numero2 = Entry(ventana)
numero2.grid(row=3, column=0)

etiqueta = Label(ventana, text='Total')
etiqueta.grid(row=4, column=0)

resultado = Entry(ventana) 
resultado.grid(row=5, column=0)

operacion = IntVar()

def calcular():
  x = int(numero1.get())
  y = int(numero2.get())

  if operacion.get() == 0:
    total = x + y
    resultado.insert(0, total)
  
  elif operacion.get() == 1:
    total = x - y
    resultado.insert(0, total)
  
  elif operacion.get() == 2:
    total = x * y
    resultado.insert(0, total)
  
  else:
    total = x / y
    resultado.insert(0, total)

botonSuma = Radiobutton(ventana, text="Sumar", value=0, variable=operacion)
botonSuma.grid(row=0, column=1)

botonResta = Radiobutton(ventana, text="Restar", value=1, variable=operacion)
botonResta.grid(row=1, column=1)

botonMultiplicar = Radiobutton(ventana, text="Multiplicar", value=2, variable=operacion)
botonMultiplicar.grid(row=2, column=1)  

botonDividir = Radiobutton(ventana, text="Dividir", value=3, variable=operacion)
botonDividir.grid(row=3, column=1)

botonCalcular = Button(ventana, text="Calcular", command=calcular)  
botonCalcular.grid(row=6, column=0)

def limpiar():
  numero1.delete(0,END)
  numero2.delete(0,END)
  resultado.delete(0,END)
  numero1.focus()
botonLimpiar=Button(ventana,text='limpiar',command=limpiar).grid(row=6,column=1)
ventana.mainloop()