from tkinter import * # * sirve para importar todos las herramientas de tk

def captura_dato():
    text=texto_nombre.get()
    mensaje= Label(ventana,text= f"hola,{text}")
    mensaje.pack()

ventana=Tk()
ventana.geometry("300x300")
ventana.title("nando")

etiqueta=Label(ventana, text="Introduce tu Nombre: ")#.grid(row=0,column=0) # sirve para colocar y ordenar filas y columnas 
etiqueta.pack()
texto_nombre=Entry(ventana)
texto_nombre.config(bg = "blue", fg="yellow") #fg es para cambiar el color de la letra
texto_nombre.pack()

boton_capturar=Button(ventana,text="Enviar", command= captura_dato)
boton_capturar.pack()

# sirve para colocar y ordenar filas y columnas 
# pack: apila y enpaqueta las etiquetas (recibe otras propiedades que grid)

ventana.mainloop() # mantiene la ventana abierta.


from tkinter import * 
ventana=Tk()
ventana.geometry("300x300")
ventana.title("nando")

def captura_edad():
    edad=int(texto_edad.get())
    if edad<=18:
        
      mensaje = Label(ventana,text="eres menor de edad")
      mensaje.pack()
    else:

     mensaje= Label(ventana,text="eres mayor de edad")
     mensaje.pack()
etiqueta=Label(ventana, text="Introduce tu Edad: ")
etiqueta.pack()

texto_edad=Entry(ventana)
texto_edad.config(bg = "blue", fg="yellow") 
texto_edad.pack()

boton_capturar=Button(ventana,text="Enviar", command= captura_edad)
boton_capturar.pack()

ventana.mainloop() 

#ULTIMO EJERCICIO
from tkinter import *

ventana = Tk()
ventana.geometry("350x400")
ventana.title('INICIAR SECION')

def evaluar_login():
    usuario=3456
    contraseña=3456
    

    text_usuario = int(Text_usuario.get())
    text_contraseña=int(Text_contraseña.get())
    if text_usuario==usuario and text_contraseña==contraseña:
        mensaje = Label(ventana, text="ingresaste")
    else:
        mensaje = Label(ventana, text="vuelve a intentar")
    mensaje.pack()
    

etiqueta = Label(ventana, text='INGRESA TU USUARIO:')
etiqueta.pack()

Text_usuario = Entry(ventana)
Text_usuario.config(bg='purple', fg='white')
Text_usuario.pack()


etiqueta = Label(ventana, text='INGRESA TU CONTRASEÑA:')
etiqueta.pack()

Text_contraseña = Entry(ventana)
Text_contraseña.config(bg='purple', fg='white',show='*')
Text_contraseña.pack()

boton_evaluar = Button(ventana, text='INGRESAR', command=evaluar_login)
boton_evaluar.pack()

ventana.mainloop()