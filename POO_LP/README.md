## PROGRAMACION ORIENTADO A OBJETOS
**EN INGLES ES OBJET ORIENT PROGRAMING**

es un programa de orientacion.

**PARADIGMA:** Es un modelo patron o ejemplo que se debe seguir.

**POO:** Es un modelo de como podemos programar.

**OBJETIVO:** El objetivo es organizar el codigo de manera que se asemeja a como pensamos en la vida real. se basa en objetos y en la **POO** un objeto es toda identidad que se puede escribir a travez de **ATRIBUTOS Y FUNCIONES** que puede realizar la identidad.

## ATRIBUTOS DE CLASE Y DE INSTANCIA
```PYTHON
class celular
```
*Atributos de tipo clases, que son iguales para todos los objetos, que se creen*
```PYTHON
familia='smart Phone'
```
*atributos de instancia, son atributos propios del objeto, creamos una funcion inicializadora*
```PYTHON
def__init__(sef,marca,modelo,emie,nroCelular):
self.marca=marca
self.modelo=modelo
self.imei=imei
self.nroCelular=nroCelular
```
**FUNCIONALIDADES**
```PYTHON
def llamar(self,destino):
  return f'llamando a {destino}'
```
**OBJETO CELULAR JORY**
```PYTHON
llamandoJory=Celular('poco','5x','2324223','945678845')
```
*Instanciando mi clase creado en mi objeto*
```PYTHON
print(llamandoJory.marca)
print(llamandoJory.familia)
print(llamandoJory.llamar('china'))
```
**OBJETO CELULAR NADINE**
```PYTHON
llamandoNadine=Celular('alcatel','basico','2387394','987674856')
print(llamandoNadine.marca)
print(llamandoJory.familia)
print(llamandoNadine.llamar('ollanta'))
```


## TAREA
1. crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
```PYTHON
tiendas=[
  {
    "ruc":28765879,
    "nombre":"el pichilon",
    "categoria":["bodega"]
    "hoario_atencion":{
      "dia":7am-12pm,
      "tarde":2pm-8pm
    }
    "gerente":"nadine"
  }
]
```
## observacion
las categorias sera 4: abarrotes,farmacias,bodega,restauran
## observacion
los gerentes solo podran ser los siguientes: edwin, china, cristian, nadine
## realizar los siguientes ejercicios
## crear la clase para tiendas que tenga los siguientes metodos uso de caso 
1. crear un metodo que me filtre las tiendas que tiene cada gerente
2. crear un metodo que me muestre los negocios que tienen mas de dos categorias
3. crear un metodo que me muestre solo el nombre y ruc de las tiendas


