## Averiguar las funciones mas 
usadas de pythpon con ejemplos
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

## AVERIGUAR SOBRE ENTORNOS VIRTUALES EN PYTHON

## ¿Qué son los entornos virtuales?
**Entornos virtuales** son entornos aislados e independientes que contienen el código y las dependencias de un proyecto.

**Pero, ¿por qué utilizar entornos virtuales?**

Pues bien, los entornos virtuales permiten instalar y utilizar distintas versiones de las mismas bibliotecas para varios proyectos. El uso de entornos virtuales también garantiza que no se produzcan cambios de última hora cuando dos o más proyectos utilicen versiones diferentes. Vamos a entender esto con más detalle.

#### **Beneficios:**

- Puedes tener varios entornos, con varios conjuntos de paquetes, sin conflictos entre ellos. De esta manera, los requisitos de diferentes proyectos se pueden satisfacer al mismo tiempo.
- Puedes lanzar fácilmente tu proyecto con sus propios módulos dependientes.
  
## HERRAMIENTAS PARA CREAR ENTORNOS VIRTUALES:


### 1. Virtualenv
Virtualenv es una de las herramientas más utilizadas para crear y gestionar entornos virtuales para proyectos Python. Un subconjunto de la funcionalidad de virtualenv está disponible en venv paquete. Sin embargo, el virtualenv es más rápido y extensible que venv.

### 2. Pipenv
Con pipnevdispone tanto de la funcionalidad de entorno virtual de virtualenv y gestión de paquetes de pip. Utiliza gestiona pipfiles para gestionar las dependencias del proyecto dentro de un entorno virtual utilizando.

Puede probar pipenv directamente desde el navegador en este Parque infantil Pipenv.

### 3. Conda
Si utiliza el Distribución Anaconda de Python para el desarrollo, puede utilizar conda para la gestión de paquetes y la creación de entornos virtuales.

Para saber más, consulte esta completa guía sobre gestión de entornos con conda.

### 4. Poesía
Poesía es una herramienta de gestión de paquetes que le permite gestionar las dependencias en todos los proyectos de Python. Para empezar a usar Poetry, necesitas tener Python 3.7 o una versión posterior instalada.

### 5. Venv
Como ya se ha dicho, venv ofrece un subconjunto de las funciones de virtualenv pero tiene la ventaja de que está integrado en la biblioteca estándar de Python, a partir de Python 3.3.

Está disponible con la instalación de Python y no requiere la instalación de paquetes externos. Lo usaremos en este tutorial para crear y trabajar con entornos virtuales. ✅