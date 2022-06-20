# Pasos para crear un proyecto en django

</br>


Vamos a crear un proyecto limpio, paso por paso
https://docs.djangoproject.com/en/4.0/


</br>

### **Creamos entorno virtual**
Creamos una carpeta donde va estar el proyecto y dentro de la carpeta tipeamos el comando. Este comando creara el entorno virtual. Antes vamos a instalar la libreria que vamos a usar. 
```
pip install pipenv 
```

Ahora vamos a ejecutar un comando y al final de la ejecucion saldra un mensaje como este
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

```
pipenv install
```

</br>

### **Corremos el entorno virtual**
Ejecutamos
```
pipenv shell
```
Esto es muy genial, ya que activa el entorno virtual por nosotros.

</br>

### **Instalamos paqutenes necesarios**
Para instalar uno o varios paquetes dentro del entorno virtual, hacemos lo siguiente.
```
pipenv install django
```

</br>

### **Ver paquetes instalados en el entorno virtual**
Para instalar uno o varios paquetes dentro del entorno virtual, hacemos lo siguiente.
```
pipenv graph
```

</br>

### **Salir del entorno virtual**
Para instalar uno o varios paquetes dentro del entorno virtual, hacemos lo siguiente.
```
exit
```

</br>

### **Instalar dependencias al estilo de npm**
Es usual que el proyecto este en un repositorio y debemos bajarlo e instalar las dependencias, En node se usa "npm install", pero en python con pipenv lo hace muy parecido.
```
pipenv install
```

</br>

### **Creamos el proyecto en django**

Le llamaremos al proyecto project1
```
django-admin startproject project1
```

Para inicializar el proyecto debemos tipiar el siguiente comando, si no configuramos al base de datos, por defecto trabajaremos con sqlite3

</br>

```
python manage.py migrate
```

</br>

### **Como Obtener ayuda**
debemos tener el entorno virtual activado.
```
manage.py help
```

</br>

### **Corremos el servidor**
Ahora para correr el proyecto tipeamos el comando. Esto es parecido al nodemos o el watch de nest, porque se queda pendiente para reiniciar, ante cualquier cambio.
```
python manage.py runserver
```

</br>

### **Como crear modulos, en este caso se llaman Apps**
En Nestjs, angular... podemos crear modulos con un comando, esto nos ayuda a modularizar nuestro proyecto y a separar las cosas, bueno en Django tambien lo podemos hacer. Nos ubicamos donde esta el archivo manage.py y tipeamos el siguiente comando, debemos cambiar  nombre_de_la_app  por el nombre que le deseamos poner a la app.
```
python manage.py startapp nombre_de_la_app
```

</br>

Importante hemos creado un modulo o una app, pero por decirlo de alguna manera, django no lo sabe, asi que debemos agregar todas las nuevas aplicaciones en el archivo settings, en la carpeta raiz del proyecto, esta el archivo settings.py, dentro hay una variable llamada INSTALLED_APPS y es un arry, dentro de ese array debemos agregar todas las apps. entre comillas escribimos el nombre que le dimos a la app y al fina de la comilla ponemos una coma  ','  
Para saber que todo esta bien, podemos probar si no hay problemas. en nombre debemos poner el nombre que le dimos a la app
```
python manage.py check nombre_de_la_app
```
deberia salir un mensaje como este:  
System check identified no issues (0 silenced).

</br>

### **Modelo para la base de datos**

Ejemplo de como crear 3 tablas de una sola app, en el archivo modules.py

```
#tabla de clientes
class Clientes(models.Model):
    nombre = models.CharField( max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=50)


#tabla de articulos
class Articulos(models.Model):
    nombre = models.CharField( max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()
    

#tabla de pedidos
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
```

Los modelos los hacemos dentro de nuestras apps. podemos crear varias tablas en una sola app. Para agregar las tablas debemos hacer las migraciones.
```
python manage.py makemigrations
```
Si todo salio bien, en este ejemplo creamos 3 tablas entonces deberia salir un mensaje como este:
 - Create model Articulos
 - Create model Clientes
 - Create model Pedidos

</br>

Aun no se han creado las bases de datos, simplemente se corrieron las migraciones, pero no se han levantado las tablas, para levantar las tablas debemos hacer lo siguiente.
```
python manage.py makemigrations
```

</br>

</br>

### **Arquitectura de Django**
Considero importante que el Framework le de una arquitectura al proyecto.  

* Se usan las apps dentro del proyecto que en otras palabras son modulos, donde estan los modelos para definir los campos de dicho modelo. Por general cada modelo corresponde a una tabla o a un documento si hablamos de No SQL. A diferencia que se pueden declarar varias tablas en un solo modelo.

</br>

</br>

</br>

</br>

</br>

### Fuentes

https://jarroba.com/pipenv-gestor-de-entornos-virtuales-de-python/
