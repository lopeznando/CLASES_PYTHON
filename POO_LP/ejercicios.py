
#haciendo uso de la POO crear un objeto para 
#la entidad celular
# class Celular:
#     marca='samsung'
#     version='año 2022'

#     def redes_sociales(self):
#         return 'hola, que haces'
#     def aplicaciones(self):
#         return 'camara,calculadora,etc'
    
# imprimir=Celular()
# print(imprimir.marca)
# print(imprimir.version)
# print(imprimir.redes_sociales())
# print(imprimir.aplicaciones())
# # #vehiculo
# class Vehiculo:
#     marca='toyota'
#     año_fabricado='2020'

#     def velocidad(self):
#         return '100 kmh'
#     def capacidad_peso(self):
#         return '5 toneladas'
    
# resultado=Vehiculo()
# print(resultado.marca)
# print(resultado.año_fabricado)
# print(resultado.velocidad())
# print(resultado.capacidad_peso())
# # #avion
# class Avion:
#     marca='ñus ñus'
#     forma='gavilan'

#     def velocidad(self):
#         return '1000 kmh'
#     def capacidad_de_pasajeros(self):
#         return '200 personas'
    
# result=Avion()
# print(result.marca)
# print(result.forma)
# print(result.capacidad_de_pasajeros())
# print(result.velocidad())
# # #freefire
# class Freefire:
#     personaje='negrito'

#     def abilidades(self):
#         return 'saltar'

# rest=Freefire()
# print(rest.personaje)
# print(rest.abilidades())
# #  #PC       
# class Pc:
#     marca='LG'
#     caracteristica='rectangular'

#     def programas(self):
#         return 'office','python'
# nando=Pc()
# print(nando.marca)
# print(nando.caracteristica)
# print(nando.programas())
# # #IMPRESORA
# class Impresora:
#     marca='Epson'
#     funcionalidad='imprimir'

#     def impresion(self):
#         return 'blanco y negro','a color'
# impri=Impresora()
# print(impri.marca)
# print(impri.funcionalidad)
# print(impri.impresion())
# # #FACTURA

# class Factura:
#     nombre='nombre del comprador'
#     DNI='DNI del comprador'
#     def igv(self):
#         return ('agregar el igv')
#     def producto(self):
#         return ('agregar mas producto')  
# fac=Factura()
# print(fac.nombre)
# print(fac.DNI)
# print(fac.igv())
# print(fac.producto())
    
# ##1. crear un objeto laptop con dos atributosde clase 
# ##y 5 atributos de instancia debera tner hasta 3 
# ##funcionalidades como minimo.

# class Laptop:
#  tamaño='16.5 pulgadas'
#  Laptop='computadora Portatil'
# def __init__(self,marca,modelo,ram,tipoDisco,almacenamiento):
#     self.marca=marca
#     self.modelo=modelo
#     self.ram=ram
#     self.tipoDisco=tipoDisco
#     self.almacenamiento=almacenamiento

# def info(self):
#     respuesta=f'''
#     ------------------------------------
# tipo:{self.tipo}
# marca | modelo | ram | tipoDisco| almacenamiento
# {self}
#     ------------------------------------


# class Mercado:
#     mercado='market'
#     def __init__(self,nroPuesto,tipoVenta,nombrePuesto,nombreDueño,horarioAtencion):
#         self.nroPuesto=nroPuesto
#         self.tipoVenta=tipoVenta
#         self.nombrePuesto=nombrePuesto
#         self.hnombreDueño=nombreDueño
#         self.hhorarioAtencion=horarioAtencion
        
# def market(self):
#         respuest=f''
#         return f'abrir el {puesto}'
#     puestoDe=Nadine('numeroPuesto:10','tipoVenta:verduras',nombrePuesto)
#     print(puestoDe)

# class Laptop:
#     tipo='Computadora portátil'
#     tamaño='13.3 o 14 pulgadas'


#     def __init__(self, marca, procesador, ram, sdd, almacenamiento):
#         self.marca=marca
#         self.procesador=procesador
#         self.ram=ram
#         self.sdd=sdd
#         self.almacenamiento=almacenamiento

    

    
#     def prender(self, ):
#         encender=f'''ENCENDIENDO LA PC
#         .............................................'''
#         return encender
#     def apagar(self, ):
#         apagado=f'''APAGANDO EL EQUIPO
#         .............................................'''
#         return apagado
#     def app(self, apk):
#         abrir_app=f'abriendo {apk} en la pc.'
#         return abrir_app
#     def info(self):
#         respuesta=f'''
#         ___________________________
#         tipo: {self.tipo}
#         marca | modelo | ram | t.disco | almacenamiento
#         {self.marca}{self.modelo}{self.ram}{self.sdd}{self.almacenamiento}
#         ___________________________'''
#         return respuesta


# equipo1=Laptop('lg','intel','8gb','128 gb','1T')
# print(equipo1.tipo)
# print(equipo1.prender)
# print(equipo1.app('canva'))


# equipo2=Laptop('hp','intel','8gb','128 gb','1T')
# print(equipo2.tipo)
# print(equipo2.apagar)
# print(equipo2.app('whatsapp'))

# equipo3=Laptop('hp','intel','8gb','128 gb','1T')
# print(equipo3.info)


    


    
    



