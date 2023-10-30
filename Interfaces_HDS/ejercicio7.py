# from tkinter import *
# ventana=Tk()
# ventana.geometry('300x300')

# etiqueta=Label(ventana,text='ingresa un numero')
# etiqueta.grid(row=0,column=0)
# num1=Entry(ventana)
# num1.grid(row=1,column=0)
# etiqueta=Label(ventana,text='ingresa un numero')
# etiqueta.grid(row=2,column=0)
# num2=Entry(ventana)
# num2.grid(row=3,column=0)
# etiqueta=Label(ventana,text='total')
# etiqueta.grid(row=4,column=0)
# total=Entry(ventana)
# total.grid(row=5,column=0)





# operacion=IntVar()

# def calcular():
#     n1=int(num1.get())
#     n2=int(num2.get())

#     if operacion.get()== 0:
#         suma=n1+n2
#         total.insert(0, suma)

#     if operacion.get()==1:
#         resta=n1-n2
#         total.insert(0,resta)

#     if operacion.get()==2:
#         multiplicacion=n1*n2
#         total.insert(0,multiplicacion)

#     else:
#         division=n1/n2
#         total.insert(0,division)

# radioSumar=Radiobutton(ventana,text="sumar",value=0,variable=operacion)
# radioSumar.grid(row=0,column=1)


# radioRestar=Radiobutton(ventana,text="restar",value=1,variable=operacion)
# radioRestar.grid(row=1,column=1)


# radioMultiplicar=Radiobutton(ventana,text=" multiplicar",value=2,variable=operacion)
# radioMultiplicar.grid(row=2,column=1)


# radioDividir=Radiobutton(ventana,text="dividir",value=3,variable=operacion)
# radioDividir.grid(row=3,column=1)


# botonCalcular=Button(ventana,text="calcular",command=calcular)
# botonCalcular.grid(row=6,column=0)

# ventana.mainloop()

# from tkinter import *

# window = Tk()
# window.geometry('300x300')

# label = Label(window, text='Enter a number')  
# label.grid(row=0, column=0)

# input1 = Entry(window)
# input1.grid(row=1, column=0)

# label = Label(window, text='Enter a number')
# label.grid(row=2, column=0)

# input2 = Entry(window) 
# input2.grid(row=3, column=0)

# label = Label(window, text='Total')
# label.grid(row=4, column=0)

# result = Entry(window)
# result.grid(row=5, column=0)

# operation = IntVar()

# def calculate():
#   x = int(input1.get())
#   y = int(input2.get())
  
#   if operation.get() == 0:
#     total = x + y
#     result.insert(0, total)
  
#   elif operation.get() == 1:
#     total = x - y
#     result.insert(0, total)
    
#   elif operation.get() == 2:
#     total = x * y
#     result.insert(0, total)
  
#   else:
#     total = x / y  
#     result.insert(0, total)

# addButton = Radiobutton(window, text="Add", value=0, variable=operation)
# addButton.grid(row=0, column=1)

# subButton = Radiobutton(window, text="Subtract", value=1, variable=operation)
# subButton.grid(row=1, column=1)

# mulButton = Radiobutton(window, text="Multiply", value=2, variable=operation)  
# mulButton.grid(row=2, column=1)

# divButton = Radiobutton(window, text="Divide", value=3, variable=operation)
# divButton.grid(row=3, column=1)

# calcButton = Button(window, text="Calculate", command=calculate)
# calcButton.grid(row=6, column=0)

# window.mainloop()

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