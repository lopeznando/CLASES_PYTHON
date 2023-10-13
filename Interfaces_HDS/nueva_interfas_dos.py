#import Tkinter
from tkinter import *
#instanciar la clase Tk()
ventana=Tk()
#creo mis dos widget de orden inferior con la clase frame()



#instancio mi primer widget
Widget_uno=Frame()
#usar metodo para montar el frame
Widget_uno.grid(row='0',column='0')
Widget_uno.config(width='100',height='100')
Widget_uno.config(bg='yellow')
#el metodo grid recibe dos parametros el numero de la columna y el numero de la fila donde quiero ubicar mi widget
#creacion del segundo widget
Widget_dos=Frame()
Widget_dos.grid(row='2',column='0')
Widget_dos.config(width='100',height='100')
Widget_dos.config(bg='purple')
#usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop() 
