# TKINTER

## QUE ES
Tkinter es una biblioteca de Python utilizada para crear interfaces gráficas de usuario (GUI, por sus siglas en inglés). Proporciona un conjunto de herramientas y widgets que permiten a los desarrolladores crear ventanas, botones, cuadros de texto y otras interfaces interactivas en sus aplicaciones. Tkinter es fácil de aprender y se utiliza ampliamente en el desarrollo de aplicaciones de escritorio en Python.

## MODO DE USO

Para utilizar Tkinter en Python, debes seguir los siguientes pasos:

1. Importar el módulo Tkinter:
```python
import tkinter as tk
```
2. Crear una instancia de la clase Tk:
```python
ventana = tk.Tk()
```
3. Agregar widgets a la ventana:
```python
etiqueta = tk.Label(ventana, text="Hola, mundo!")
   boton = tk.Button(ventana, text="Haz clic")
```
4. Organizar los widgets en la ventana utilizando algún sistema de geometría, como grid, pack o place:
```python
etiqueta.pack()
   boton.pack()
```
5. Iniciar el bucle principal de la aplicación:
```python
ventana.mainloop()
```
Estos pasos básicos te permitirán crear una ventana con algunos widgets utilizando Tkinter. A partir de aquí, puedes explorar la documentación de Tkinter para aprender sobre otros widgets, eventos, propiedades y métodos disponibles para personalizar y mejorar tus aplicaciones de GUI.