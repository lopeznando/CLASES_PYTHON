alumnos=[
    {
        'id':1,
        'nombre':'edwin',
        'apellido':'ramos aguilar',
        'DNI':2368283,
        'curso favorito':'lenguaje',
    }
]
class Alumno:
    
 def __init__(self,nombre,apellido,DNI,cursoFavorito):
        self.nombre=nombre
        self.apellido=apellido
        self.DNI=DNI
        self.cursoFavorito=cursoFavorito
    
 def mostrar_alumnos(self):
        mensaje=f"""
        tienes {len(alumnos)} alumnos los alumnos son:{alumnos}"""
        return mensaje
 
 def registrar_alumno(self):
        nuevo_id=len(alumnos)+1
        alumno_nuevo={
            "id":nuevo_id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "DNI":self.DNI,
            "cursoFavorito":self.cursoFavorito
        }
        registro_alumno=alumnos.append
        (alumno_nuevo)
        return f"el siguiente alumno se registro exitosamente{alumno_nuevo}"
def mostrar_alumnos(self,id):
        alumno_buscar=alumnos[id-1]
        return alumno_buscar
def eliminar_alumno(self,id):
        alumno_iliminar=alumnos.pop(id-1)
        return f"el siguiente alumno fue elimindo{alumno_iliminar}"
def actualizar_alumno(self,id,clave,valor):
      ol=valor
      producto_actualizar=list(filter(lambda el: el[clave]==id,alumnos))[0].update
      ({clave:valor})
      return "se actualizo"
    

alum=Alumno('cristian','poma ramos',2445343,'desarrollo')
print(alum.registrar_alumno())
print(alum.mostrar_alumnos())
print(alum.mostrar_alumnos(1))
print(alum.eliminar_alumno(2))
print(alum.mostrar_alumnos())

    