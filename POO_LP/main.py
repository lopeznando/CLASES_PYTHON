
#el nombre siempre debera ser en singular y 
#con la primera letra en MAYUSCULA
class Perro:
    nombre='boby'
    edad='2 meses'
    color='cheqche'
    raza='pequeñez'
# OJO siempre cuando trabajes con un objeto debera
#ir en el primer parametro el comando SELF
    def ladrar(self):
        return 'gua gua mascota'
    def correr(self):
        return '......'
    
respuesta=Perro()
print(respuesta.nombre)
print(respuesta.ladrar())
print(respuesta.correr())