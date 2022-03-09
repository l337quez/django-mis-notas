# django-mis-notas

</br>

### Para crear un proyecto
* Le llamaremos al pryecto project1  
``` 
django-admin startproject project1
``` 

* Para inicializar el proyecto debemos tipiar el siguiente comando, si no configuramos al base de datos, or defecto trabajaremos con sqlite3

</br>

``` 
python manage.py migrate 
``` 

### Para correr el servidor
Cuando se vuelva a correr el proyecto es necesario activar
la virtaulenv. se debe hacer en la carpeta principal es decir en django-mins-notas. Si esto no esta activado no se podra ejecutar el servidor.


``` 
source ./firts_project/bin/activate

``` 

Luego si podremos correr el servidor.

``` 
python manage.py runserver
```

</br>



### Estrucutra de carpetas y archivos de Django

* urls:  es donde se guardan las rutas. Las rutas se guardan en una tupla y por defecto se encuentra la ruta 'admin/'.

</br>

Ejemplo: vamos a crear una ruta llamada 'saludo' que llama a la funcion saludo. La funcion saludo esta en el archivo views, por lo tanto hay que importar la ruta del view en el archvo urls
    path('saludo/', saludo),