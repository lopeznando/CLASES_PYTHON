# #lambda una funcion que se subejecuta
# hola=lambda a,b:print(a+b)
# #funcion normal
# def suma(a,b):
#     print(a+b)
# suma(4,6)
# hola(10,20)

# #if ternario
# ternario="soy verdad ternario" if True else "soy flaso ternario"
# print(ternario)
# if True:
#     print("soy verdad")
# else:
#     print("soy mentira")

# ##FILTER

# lista_alumnos=[
#     {
#         "nombre":"edwin",
#         "edad":15,
#         "hobby":"danza",
#         "flaquita":"melody"
#     },
#     {
#         "nombre":"del mar",
#         "edad":30,
#         "hobby":"saltar",
#         "flaquita":"melody"
#     },
#     {
#         "nombre":"nando",
#         "edad":14,
#         "hobby":"ponchar",
#         "flaquita":"sami"
#     },
#     {
#         "nombre":"jory",
#         "edad":50,
#         "hobby":"aplicar",
#         "flaquita":"hermana"
#     }
# ]
# # print(f"todosmis alumnitos{lista_alumnos}")
# fans_melody=list(filter(lambda par:par["flaquita"]=="melody",lista_alumnos))
# print(f"los que quieren con melody{fans_melody}")

# #MAP
# # nuevo_objet=list(map(lambda par:{"nombre_alumno":par["nombre"],"germita":par["flaquita"]},lista_alumnos))
# # print(nuevo_objet)


from bd import *
class Puestos_gerente:
    def puesto1_gerente(self,bd_puesto_gerente,nombre_gerente):
        respuesta=list(filter(lambda el:el["gerente"]==nombre_gerente,bd_puesto_gerente))
        return respuesta 
gerente=Puestos_gerente() 

print(gerente.puesto1_gerente(puesto_gerente,"china"))
print(gerente.puesto_mas_categorias(puesto_gerente))
print(gerente.ruc_nombre(puesto_gerente))


def puesto_mas_categorias(self,bd_puesto_gerente):
    respuesta=list(filter(lambda el:len(el["categoria"])>2,bd_puesto_gerente))
    return respuesta


def ruc_nombre(self,bd_puesto_gerente):
    respuesta=list(map(lambda el:{
        "nombre_puesto":el["nombre"],
        "ruc_puesto":el["ruc"]
    },bd_puesto_gerente))

def eliminar_puesto(self,bd_puesto_gerente,ruc):
    respuesta=list(filter(lambda el:el["ruc"]!=ruc,bd_puesto_gerente))
    return respuesta

def actualizar_puesto(self,bd_puesto_gerente,ruc,clave,valor):
    respuesta=list(filter(lambda el:el))