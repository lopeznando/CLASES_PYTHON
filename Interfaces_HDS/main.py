import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")

etiqueta = tk.Label(ventana, text="¡hola nando!")
etiqueta.pack()

ventana.mainloop()