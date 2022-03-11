# django-mis-notas

</br>

**Creaste el proyecto y ahora debes hacer algo como npm install, pero en python**  
En node se hace un npm install y con eso instalamos todo lo que se encuentra en el archivo "package.json". Debemos instalar pipenv para obtener algo parecido a la funcionalidad de node. Asi que vamos a instalar un instalador de paquetes. Usando este paquete no es necesario crear una virtualenv.

``` 
pip install pipenv
``` 
Debemos configurar el path seguir tutorial
https://koenwoortman-com.translate.goog/python-pipenv-command-not-found/?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es-419

</br>

CURISIDADES:  
Podemos instalar paquetes de node en python  
source ./bin/activate  
pip install nodeenv  
nodeenv -p

</br>

### creaste una virtual env sin pipenv
Seguramente necesitas las dependencias del proyecto  
``` 
pip list --format=freeze > requirements.txt
``` 

</br>

### Para crear un proyecto
Lo ideal es crear un entorno virtual de python, eso tambien se hace en node, es importante porque guarda las versiones de las librerias y todo lo que se este usando en el proyecto. Al crear un pyenv, se crearan unas carpetas que se llaman bin y lib, entonces en la ruta donde estan esas carpetas esta el entorno virtual, esto es como en recordatorio, ya que debemos activar el entorno para instalar una libreria nueva. 

Coomenzamos creando el proyecto.

* Le llamaremos al proyecto project1  
``` 
django-admin startproject project1
``` 

* Para inicializar el proyecto debemos tipiar el siguiente comando, si no configuramos al base de datos, or defecto trabajaremos con sqlite3

</br>

``` 
python manage.py migrate 
``` 

</br>

### Desactivar la virtualenv
``` 
deactivate
``` 

### Para correr el servidor
Cuando se vuelva a correr el proyecto es necesario activar
la virtaulenv. se debe hacer en la carpeta principal es decir en django-mins-notas. Si esto no esta activado no se podra ejecutar el servidor.


``` 
source ./firts_project/bin/activate

``` 
cuando se activa le virtualevn en la terminal saldra el nombre que se le dio antes del promt.

</br>

Luego si podremos correr el servidor. Debemos ubicarnos en la ruta donde esta el archivo "manage.py"

``` 
python manage.py runserver
```

</br>



### Estrucutra de carpetas y archivos de Django

* urls:  es donde se guardan las rutas. Las rutas se guardan en una tupla y por defecto se encuentra la ruta 'admin/'.

</br>

Ejemplo: vamos a crear una ruta llamada 'saludo' que llama a la funcion saludo. La funcion saludo esta en el archivo views, por lo tanto hay que importar la ruta del view en el archvo urls
    path('saludo/', saludo),
