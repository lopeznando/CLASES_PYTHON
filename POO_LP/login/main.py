
from bd import * 
class Usuario:

    def __init__(self, dni, nombre, f_nacimiento, edad,usuario, password):
        self.dni=dni
        self.nombre=nombre
        self.f_nacimiento=f_nacimiento
        self.edad=edad
        self.usuario=usuario
        self.password=password

    def mostrar_usuario(self, ide):
        resultado=list(filter(lambda par:par['dni']==ide,usuarios))
        return f'''informacion del usuario que buscas:
    _____________________________________________________________________________________________________
        {resultado}'''
    
    def agregar_edad(self, clave, valor):
        for usuario in usuarios:
            if usuario['dni'] == self.dni:
                usuario[clave] = valor
        return 'Usuario encontrado.'

    def verificar_usuario(self, usuario_buscar):
        for usuario in usuarios:
            if usuario['usuario'] == usuario_buscar:
                return 'Usuario registrado.'
        return 'Usuario no encontrado en los registros.'

    def validar_usuario_password(self, usuario_a_validar, password_a_validar):
        for usuario in usuarios:
            if usuario['usuario'] == usuario_a_validar and usuario['password'] == password_a_validar:
                return 'Usuario y contraseña válidos.'
        return 'Usuario o contraseña incorrectos.'

ac=Usuario(71439102,"jhonatan","10/07/2004",None,"jhonita","12345")
print(ac.agregar_edad("edad", 20))
print(ac.mostrar_usuario(124567))

usuario_a_buscar = "jhonita"
print(ac.verificar_usuario(usuario_a_buscar))
print(ac.mostrar_usuario(124567))

usuario_a_validar = "jhonita"
password_a_validar = "12345"
print(ac.validar_usuario_password(usuario_a_validar, password_a_validar))
print(ac.mostrar_usuario(124567))