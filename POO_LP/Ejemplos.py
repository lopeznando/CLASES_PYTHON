
productos=[
    {
        "id":"1",
        "nombre":"arroz",
        "descripcion":"costeño costal x 100 kg",
        "stock":5,
        "unidad":"costales",
        "precio":125,
        "moneda":"soles"
    }
]

# casos de uso
class Producto:
    # atributos de instancia
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda
    # creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""tienes {len(productos)} productos los productos son: {productos}"""
        return mensaje
    
    def registrar_producto(self):
        nuevo_id=len(productos)+1
        producto_nuevo={
            "id":nuevo_id,
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "stock":self.stock,
            "unidad":self.unidad,
            "precio":self.precio,
            "moneda":self.moneda
        }
        registro_producto=productos.append(producto_nuevo)
        return f"el siguiente producto se registro exitosamente{producto_nuevo}"
    
    def mostrar_producto(self,id):
        producto_buscar=productos[id-1]
        return producto_buscar
    
    def eliminar_producto(delf,id):
        producto_eliminar=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminar}"
    
    def actualizar_producto(self,id,clave,valor):
        el=valor
        producto_actualizar=list(filter(lambda el: el[clave]==id,productos))[0].update({clave:valor}) #["h","o","l","a"]
        return "se actualizo"

# programacion funcional en python
# metodo funcional filter retona una lista con el elemento que se true de una lista
# funciones anonimas o autoejecutadas en python se les conoce como funciones lambda -> una funcion anonima
# su uso estructura
# lambda a,b:return a+b # esta funcion se autoejecuta no se llama
# suma=lambda a,b: retun a+b # para erar esta funcion necesita llamar al variable suma
# suma(3,7)

prod=Producto("aceite","extra virgen",2,"botella litro",12.50)
print(prod.registrar_producto())
print(prod.mostrar_productos())
# print(prod.mostrar_producto(1))
# print(prod.eliminar_producto(2))
# print(prod.mostrar_productos())
print(prod.actualizar_producto(125,"precio",130))
print(prod.mostrar_productos())
#lis funcion para crear lista

