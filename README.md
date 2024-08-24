﻿# Prueba-Tecnica-Python-Pro
## Prueba tecnica para Kodland
Aplicación para ser tutor de Python Pro en Kodland

### Funciones Generales
Primero cree una carpeta en la cual es se creará el entorno virtual, en el VScode, al haber ingresado en la carpeta de trabajo
cree una terminal en la que instale virtualenv, en el cual instalé todas las librerías necesarias para crear este proyecto.

las librerias que usé son: flask, flask_mysqldb, config, math, json, ast, django

Esta es una aplicación para el conteo de entradas y salidas, y su metodo de pago en una entrada de trasmilenio

###Aplicación
Primero se define las funciones de las librerias que se va a usar, en el apartado de config.py se realizar el enlace a la base de datos MySQL en la que se almacenará todos los registros de la aplicación.
Se crea el archivo app.py donde se realiza la configuración de la pagina web para que se recargue cada vez que se recargue la pagina para no tener que parar y ejecutar nuevamente la aplicación.
Se crea un decorador el cual siempre retornará la pagina principal de la aplicación, en esta se crea una funcion Index, en la cual se utiliza el metodo de Get de MySQL para retornar los datos a la pagina principal la cual es creada en la carpeta template, con nombre de index.html. En esta sección se crea un Appyrest en la cual tiene los metodos para adquirir, agregar, editar y eliminar archivos de la base de datos en MySQL

En index.html se encuentra el front de la aplicación donde se encontra la elección que tomará cada usuario que entra a la parada de trasmilenio, las cuales serán guardadas con su nombre respectivo para ser importados a la base de datos, de la cual tambien se crea una tabla para mostrar esta base de datos con la opción de editar o eliminar a cada uno de los elementos, ademas se encuentra un enlace entre los archivos como extenciones a travez de la programación de django

el archivo principal que conecta todos los archivos el layout.html, en el cual se utiliza el motor de plantilla jinja 2 para realizar la distribución y estilo a traves de bootstrap, dibidiendo en clases todas las secciones.

En count.html se muestra los resultados finales contados y transmitidos desde app.py
En editar.html se muestra el ingreso de datos muy parecido a como se muestra en index, pero sin la tabla, donde se edita el dato seleccionado.








