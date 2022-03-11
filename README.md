# Pasos para crear un proyecto en django

</br>


Vamos a crear un proyecto limpio, paso por paso
https://docs.djangoproject.com/en/4.0/


</br>

### **Creamos entorno virtual**
Creamos una carpeta donde va estar el proyecto y dentro de la carpeta tipeamos el comando. Este comando creara el entorno virtual. Al final de la ejecucion saldra un mensaje como este
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
Es usual que el proyecto este en un repositorio y debemos bajarlo e instalar las dependencias, En node se usa "npm install", pero en python con pipenv lo asi muy parecido.
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

</br>

</br>

### Fuentes

https://jarroba.com/pipenv-gestor-de-entornos-virtuales-de-python/
