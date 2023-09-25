## Crear un programa que me pida edad de una persona, 
# si la edad es mayor a 18 que muestre un menssaje 'Eres mayor de edad'
#caso contrario que muestre un mensaje 'Eres menor de edad'.


# nombre=input(' Ingrese su nombre: ')
# edad = int(input("Ingresa tu edad: "))
# if edad>=18:
#         print( nombre + ' ' + 'Eres mayor de edad')
# else:
#     print(nombre + ' ' +'Eres menor de edad')
    

# Una tienda comercial desea hacer un descuento del 20%, crear un programa  que me determine si el cliente se hace acreedor
#del descuento teniendo en cuenta los  siiguiente: si el cliente realiza una compra de ygual o mayor a s/. 1000 soles  mostrar un mensaje que diga 
# 'GANASTE EL DESCUENTO DE20%, AHORA PAGARAS <mostar el total de   la compra menos el descuento>' en caso la compra o supere los S/.1000 soles  entonses 
#mostrar un mensaje que diga'NO APLICAS AL DESCUENTO <mostar el monto de la compra'

# NOM_TIENDA= "COMERCIAL JUELICIANA "
# NOM_CLIENTE=input ('Ingrese su nmbre: ')
# MONT_COMPRA= int(input('Ingresa el monto de compra: '))
# if MONT_COMPRA>= 1000:
#         descuento = MONT_COMPRA * 0.2
#         total_pagar = MONT_COMPRA - descuento
#         print(f"¡GANASTE EL DESCUENTO DE 20%! Ahora pagarás {total_pagar} soles.")
# else:
#         print(f"NO APLICAS AL DESCUENTO. El monto de la compra es de {MONT_COMPRA} soles.")

# crear un programa que me pida 5 veces un nombre y por cada ve que lo pida muestre la cantidad de 
# veces que ingreso el nombre 

# for n in range(1,6):
#        nombre=input("ingrese un nombre: ")
#        print(f"ingresaste {n} veces el nombre")

# crear un programa que pida un numero y lo evalue con el numero premiado si el numero
# ingresado es el premiado el programa finalizara si el numero ingresado es incorrecto 
# el programa seguira pidiendo el numero premiado 

# numero_ganador=10
# condicion=True
# while condicion:
#        numero_ingresado=int(input("ingrese un numero: "))
#        if numero_ingresado==numero_ganador:
#               print("ganste")
#               condicion=False
#        else:
#               ("sigue intentando")


# lista=[12,3,4,34,2]
# mi_print(min(lista))

# def mi_min(lista):
#     numero_menor=lista[0]
#     for numero < numeroi_menor:
#     numero_menor=numero
#     return numero_menor
# print(mi_min(lista))

##crear una funcion por cada operador aritmetico que resiva 
##dos parametros y retorne el resultado de la operacion. crearse
##una funcion que nos permita imprimir el resultado 
# a=int(input(" SAIRE INGRESE EL NUMERO: "))
# b=int(input(" SAIRE INGRESE EL NUMERO: "))
# def suma(a,b):
#     total=a+b
#     return total
# print(suma(a,b))


# def resta(a,b):
#     total=a-b
#     return total
# print(resta(a,b))

# def multiplicar(a,b):
#     total=a*b
#     return total
# print(multiplicar(a,b))

# def dividir(a,b):
#     total=a/b
#     return total
# print(dividir(a,b))

##escribe una funcion que reciba un numero entero positivo
##y devuelva su factorial
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingresa un número entero positivo: "))
resultado = factorial(numero)
print("El factorial de", numero, "es", resultado)
## escribir una funcion que resiva como parametros una 
##una lista de numeros y retorne una nueva lista con cada 
##numero elevados al cuadrado.
def elevar_al_cuadrado(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero ** 2)
    return nueva_lista
##Escribir un programa que reciba una cadena de caracteres
##y devuelva un objeto con cada palabra que contiene y su 
##frecuencia
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

cadena = input("Ingresa una cadena de caracteres: ")
frecuencia_palabras = contar_palabras(cadena)
print(frecuencia_palabras)