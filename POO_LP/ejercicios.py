
#haciendo uso de la POO crear un objeto para 
#la entidad celular
class Celular:
    marca='samsung'
    version='año 2022'

    def redes_sociales(self):
        return 'hola, que haces'
    def aplicaciones(self):
        return 'camara,calculadora,etc'
    
imprimir=Celular()
print(imprimir.marca)
print(imprimir.version)
print(imprimir.redes_sociales())
print(imprimir.aplicaciones())
#vehiculo
class Vehiculo:
    marca='toyota'
    año_fabricado='2020'

    def velocidad(self):
        return '100 kmh'
    def capacidad_peso(self):
        return '5 toneladas'
    
resultado=Vehiculo()
print(resultado.marca)
print(resultado.año_fabricado)
print(resultado.velocidad())
print(resultado.capacidad_peso())
#avion
class Avion:
    marca='ñus ñus'
    forma='gavilan'

    def velocidad():
        return '1000 kmh'
    def capacidad_de_pasajeros():
        return '200 personas'
    
result=Avion()
print(result.marca)
print(result.forma)
print(result.capacidad_de_pasajeros())
print(result.velocidad())
#freefire
class Freefire:
    personaje='negrito'

    def abilidades():
        return 'saltar'

rest=Freefire()
print(rest.personaje)
print(rest.abilidades())

        
