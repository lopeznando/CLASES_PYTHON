# REPASO PYTHON


## TIPOS DE DATOS
  **Tipos  de datos primitivos**
 ```python
 'a' # string cadena texto
 'hola' # esto tambien es un string
 'hola soy un string y te saludo' # cadena larga
 ```
**OBSERVACION :**  *Todo lo que este entre comillas  es un* **string**.

```python
'100'
'false'
"hola"
```
*Aun string puede estar entre comillas dobles ("") o comillas simples (´´)*
```python
100 # esto es un tipo de dato numerico entero intiger 
2.1  # Esto es un dato de tipo numerico de tipo flotante Float
```





## VARIABLES
*Es donde almacenamos nuestro tipo de dato,estos datos pueden **mutar cambiar o modificarse** como creamos una variable para almacenar nuestros datos.*
1. Darle un nombre **significativo** o relacionado al dato que estamos almacenando.
2. Indicar el tipo de dato esta relacionado → asignacion =.
3. Indicar el tipo de dato que se va almacenar → darle el dato a guardar.

```python
# primero el dato lo voy a pedir la edad a nadine
edad_nadine=18

#El nombre de un alumno
 nombre_alumno='Edwin'
```

## OPERADORES
1. Existen los operadores aritmetico
 * suma 
 * resta
 * multiplicacion
 * divicion
  
 **SUMA**
```PYTHON
Suma = 45+12
```
**RESTA**
```PYTHON
Resta = 45-12
```
**MULTIPLICACION**
```PYTHON
Multiplicacion =45*12
```
**DIVICION**
```PYTHON
 Divcion = 45/12
```

```PYTHON
operacion=(45+12+23)/4
op=15+12+14+13/4
#Presedencia de operadores
```
### OPERADORES DE  DE USO ESPECIAL
```PYTHON
# OPERADOR DE USO ESPECIAL (SUMA)
suma=45+47 # Operador suma resultado 87
suma='45' + 12 # Operador  concatenacion resultado 4512
saludo= 'Hola'+'Mundo' # concatenacion HolaMundo
saludo2='Hola'+''+'Mundo' # concatenar Hola Mundo
# OPERADOR DE USO ESPECIAL (MULTIPLICAR)
saludos='hola'*2 #holahola
saludo1s='hola '*2 #hola hola
```


## DATOS ESTRUCTURADOS

## LISTAS
Se puede almacenar distintos tipos de datos en una sola lista separados por coma.

```PYTHON
 Lista=['nombre',10, False]
 Lista_amigos=['jory','ñawi','adan','chinita']
```
## OBJETOS

Tambien al ygual que las listas almacenas distintos tipos de dstos, pero con un orden.

Para almacenar datos de un objeto nesesitamos especificar in indice y un valor indice →valor
```PYTHON
{
    'nombre':'jory',
    'edad':54
    'sexo' : 'todos los dias'
}
###################################
#combinar ambas estructura de datos
alumno={
    'nombre':'jory',
    'edad':54
    'amigos': [ 'antony','edwin','china'],
    'direccion':{
        'departamento': 'ayacucho',
        'provincia': 'lucanas',
        'distrito': 'puquio',
        'jiron': ' cusco',
        'numero':125

    }
}
 alumnos=[{},{},{}]
```
## CONTROLES DEN FLUJO
### DECISIONES
Solo se ejecuta el codigo si cumple la condicion es verdadera,  podemas hacer si la condicion sea falsa se ejeute otro codigo.

**SINTAXIS**

Primero especificar el codigo que ejecutara si cumple una condicion
```PYTHON
if <condicion>:
    ## El codigo que deseamos ejecutar si la condicion es verdad
    print('Ejecuta esto')
## Aqui estamos fuera del if o del si este codigo siemprese ejecutara no depende del if
print('Esto siempre ejecutara')
#---------------------------------------------------------------------
# Si queremos que se ejecute un codigo en caso sea falso
if <condicion falsa>:
    print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
```
**EJEMPLITOS**

```PYTHON
if 15>18:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
if 15*2==30:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
condicion= True
if  condicion:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```



## CICLOS
**EXISTEN  DOS TIPOS**

* Cuando sabemos la cantidad de veses que vamos a repetir algo.
Para este caso existe el **FOR**. Sintaxis despues de la palabra reservada **FOR**  deberemos crear una variable que almacene el numero que iremos intentando.luego tendremos que indicar el rango a intentar a los elementos a intentar.
```PYTHON
for i in range(1,5):
    print(i)
```
```PYTHON
vocales=['a','e','i','o','u']
for i in vocales:
    print (i)
```
```PYTHON
numeros=['45','12','78','1','2']
for i in numeros:
    print (i)
```
## FUNCIONES
**Existen dos funciones**
1. **PROPIAS DEL LENGUAJE**
   
   Que ya vienen creadas ye insertadas en **PYTHON**  y estan listas para ser usadas

   *Estructura de uso de una funcion*
    
    tiene el nombre seguido de parentises
    dentro de paretisis ódemos pasarle datos que nesesita la funcion para ejecutarse
    . Esta funcion que nos sirve para  para mostar por consola de datos.
```PYTHON
print ('hola')
```
**LEN**

Esta funcion nos permite saber la longuitud de una lista o un strung **LEN** nos debuelve un numero
```PYTHON
print (len([1,5,6,7,8]))
```
Es una funcion que se detiene a esperar que el usuario introdusca informacion
Entre parentisis podemos escribir un mensaje que indique la accion que realizara el usuario.
```PYTHON
input
```
**FUNCION APPEND**

funcion de python nos permite agregar elementos al final de la lista

```PYTHON
lista=[15,12,78]
elemento=100
lista.append(elemento)
print(lista)
```
**FUNCION POP**

funcion de python que nos permite eliminar los elementos que encuentran al final de una lista
y los almacena dentro de ello
```PYTHON
lista=[15,12,78]
lista.pop( )
print(lista)
```
**FUNCION INSERT**

funcion de python que nos permite agregar elemnetos en cualquier posicion de mi loista para eso se le tiene que pasar dos paramentros, primero indicarle el indice y segundo el otro dato que se va agregar
```PYTHON
lista_nombres=["jory","nadine","bichota"]
lista_nombres.insert(1,"santan")
print(lista_nombres)
```
**FUNCION REMOVE**

funcion de python que nos permite eliminar elementos de cualquier pocision de una lista, esta funcion recibe solo el elemento que deseamos eliminar 
```PYTHON
lista=[4,5,6,8,6,7]
lista.remove(6)
print(lista)
```
**FUNCION SPLIT**

funcion que nos permite dividir en una lista una cadena
```PYTHON
cadena="hola como estan"
lista=cadena.split( )
print(lista)
url="www.google.com/id=79273"
id=url.split("=").pop()
print(id)
```

1. **FUNCIONES CREADAS (PROPIAS)**

pasos para crear una funcio propia

1. hacer uso de la palabra reservada DEF.
2. definir un nombre de funcion que descruba que tarea va a realizar.
3. establecer los paramertros de que servira la funcion entre parebtesis ().
4. establecer que valor o dato va retornar mi funcion con la palbra reservada return #> Observacion =>> tambien podemos hacer uso de la funcion print () para retornar un mensaje en nuestra funcion.

Existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros
```PYTHON
def saludo():
 print("hola este es un saludo)
```
como hacemos uso de la funcion

nombre de la funcion y parentesis

funcion con parametros
```PYTHON
def mi_print(texto):
 print(texto)
```
print("hola este print de python")

mi_print("hola este es mi print de python")

```PYTHON
def suma(a,b):
    total=a+b
    return total

mi_print(suma(45,12))#==>>>>>
```
```PYTHON
def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
     if numero > numero_mayor:
        numero_mayor=numero
    return numero_mayor
mi_print(mi_max(lista))
```
**FUNCIONES CON MUCHOS PARAMETROS**
```PYTHON
def funcion(muchis_parametros):
    total=0
    for numero in muchos_numeros:
        total=total+numero
        return total
print(funcion(45,34,33,37,45))
```
```PYTHON
def datos(*argumentos):
    nombre=argumentos[0]
    apellido=argumentos[1]
    edad=argumentos[2]
 return f' mi nombre es,{nombre},{apellido}y mi edad es,{edad}'
 print(datos('edwin','apellido','50'))
 