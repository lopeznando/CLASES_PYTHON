# ENTORNOS VIRTUALES
**PIENV**

Es un manejador de versiones de python.

**PIPENV**

Creador de entornos virtuales desfasado ya no se usa.

**COMO CREAR UN ENTORNO VIRTUAL**

1. Nos uvicamos en la carpeta que deseamos crear el entorno virtual.

```bash
cd < ruta del archivo >
#ejemplo
cd nombre_carpeta/entorno_uno
```
2. creamos el entorno virtual con el siguente virtual
```bash
python -m venv <nombre de nuestro entorno virtual>
#ejemplo
python -m venv mi_entorno
```
3. para activar el entorno virtual con el gitbash como terminal predeterminada corremos al siguente comando solo para windows
```bash
source venv/script/activate
```
## PARA ACTIVAR EN POWERSHELL
para poder ejecutarlo en powershell como terminal predeterminado ejecutar el siguiente comando.
```bash
venv\Scripts\Activate.ps1
```
## PARA INSTALAR PAQUETES EN NUESTRO ENTORNO VIRTUAL
primero verificamos que no tengamos el paquete instaldo y lo listamos con el sigiente comando. Debemos tener activado nuestro entorno virtual.
```bash
pip list
```
luego instalaremos con el siguente comando
```bash
pip install <nombre del paquete>
#ejemplo
pip install pandas
```
