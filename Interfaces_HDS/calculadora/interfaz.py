from tkinter import*
from funciones import*
root=Tk()
root.title("Calculadora")
root.geometry("296x310")
root.resizable(0,0)

pantalla=Entry(root,
               width=22,
               bg="sky blue",#asigna el color de fondo
               fg="white",#asigna el color de letra
               borderwidth=0,#tamaño de borde del cuadro de mi texto
               font=("arial",18,"bold"))#asignamos el tipo y tamaño de fuente
pantalla.grid(row=0,columnspan=4,padx=4,pady=4)
##añadir los botonos a mi calculadora
boton_1=Button(root,text="1",
               width=9,#hancho
               height=3,#altura
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(1,pantalla)).grid(row=1,column=0,padx=1,pady=1)#cursor sirve para cambiar el estilo del mouse
boton_2=Button(root,text="2",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(2,pantalla)).grid(row=1,column=1,padx=1,pady=1)

boton_3=Button(root,text="3",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(3,pantalla)).grid(row=1,column=2,padx=1,pady=1)

boton_4=Button(root,text="4",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(4,pantalla)).grid(row=2,column=0,padx=1,pady=1)

boton_5=Button(root,text="5",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(5,pantalla)).grid(row=2,column=1,padx=1,pady=1)

boton_6=Button(root,text="6",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(6,pantalla)).grid(row=2,column=2,padx=1,pady=1)

boton_7=Button(root,text="7",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(7,pantalla)).grid(row=3,column=0,padx=1,pady=1)

boton_8=Button(root,text="8",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(8,pantalla)).grid(row=3,column=1,padx=1,pady=1)

boton_9=Button(root,text="9",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(9,pantalla)).grid(row=3,column=2,padx=1,pady=1)

boton_0=Button(root,text="0",
               width=9,
               height=3,
               bg="white",
               fg="black",
               borderwidth=0,
               cursor="hand2",
               command=lambda:enviar_boton(0,pantalla)).grid(row=4,column=1,padx=1,pady=1)

boton_igual = Button(root,text="=",
				width=9,
				height=3,
				bg="red",
				fg="white",
				borderwidth=0,
				cursor="hand2",
        command=lambda: igual(pantalla)).grid(row=4, column=0, padx=1, pady=1)

boton_punto = Button(root,text=".",
				width=9,
				height=3,
				bg="spring green",
				fg="black",
				cursor="hand2",
				borderwidth=0,
        command=lambda:enviar_boton(".",pantalla)).grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root,text="+",
				width=9,
				height=3,
				bg="deep sky blue",
				fg="black",
				borderwidth=0,
				cursor="hand2",
        command=lambda:operacion("+",pantalla)).grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root,text="-",
				width=9,
				height=3,
				bg="deep sky blue",
				fg="black",
				borderwidth=0,
				cursor="hand2",
        command=lambda:operacion("-",pantalla)).grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root,text="*",
				width=9,
				height=3,
				bg="deep sky blue",
				fg="black",
				borderwidth=0,
				cursor="hand2",
        command=lambda:operacion("*",pantalla)).grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root,text="/",
				width=9,
				height=3,
				bg="deep sky blue",
				fg="black",
				borderwidth=0,
				cursor="hand2",
        command=lambda:operacion("/",pantalla)).grid(row=4, column=3, padx=1, pady=1)

boton_limpiar = Button(root,text="Limpiar",
				width=40,
				height=3,
				bg="deep sky blue",
				fg="black",
				borderwidth=0,
				cursor="hand2",
				command=lambda:limpiar(pantalla)).grid(row=5, column=0, columnspan=4, padx=1, pady=1)


mainloop()