
---

# Gestionador dinámico de repositorios

***

El presente script permite navegar de forma eficiente un listado de repositorios, con la finalidad de hacer una gestión en particular, de una forma rápida y cómoda, priorizando el orden.

***

## Uso comprodado en gestión de repositorios

Este Script me permitió gestionar de forma rápida y eficiente las vulnerabilidades fluid que hacían referencia a problemas de seguridad en más de 28 proyectos en tan solo un día de trabajo, así como los cambios que se presentarán durante mi gestión. Espero que este aporte sea de utilidad.

## Descripción del archivo de programación de navegación eficiente:
En el archivo <b>gestion_microservicios.txt</b> hay una tabla donde se visualizan tres columnas separadas por “|”.

<ul>
<li>La primera columna hace referencia al nombre del proyecto.</li>
<li>La segunda columna son valores boleanos que hace referencia a la gestión realizada. 0 (Url gestionada) y 1 (Url no gestionada).</li>
<li>La tercera columna hace referencia a la URL a ser vistada.</li>
</ul>

## Que hace este programa:

<ul>
<li>Recorrer uno a uno los registros.</li>
<li>Abre la url asignada a traves de un navegador construido por python usando la librería <b>webview</b>.</li> 
<li>El usuario hará en dicho sitio web la tarea que desea realizar.</li>
<li>Luego, cerrará la ventana del navegador construido por python.</li>
<li>Y automaticamente, el programa pide por consola el resultado de la gestión realizada.</li>
<li>El usuario debe responder: 1 (Gestionado) y 0 (No gestionado).</li>
<li>Luego de presionar Enter, automáticamente se abrirá la ventana de navegación del siguiente registro.</li></ul>

De esta manera, se irán gestionando todas las URL del listado.
Una vez recorrido todos los registros, el programa revisa si hay registros todavía en cero, sin gestión, y los recorre de nuevo, hasta que el usuario reporte todas la URL como gestionadas.

## Modo de uso por consola
<pre>
python -m venv env
./env/Scripts/activate
python -m pip install --upgrade pip
pip install pywebview
py main.py
</pre>

---

## Realice sus pruebas, actualizaciones o modificaciones.
Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

## Actualizar la receta.
Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```

---

## Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |

***

## Librerías del proyecto.
| librería | Descripción| Comando |
| :---- | :--- | :--- |
| webview | Crea una navegador web independiente. | pip install pywebview |

Con la instalación de la librerÍa <b>pywebview</b> se instalarán las
siguientes librerías de manera automática:

<pre>
bottle==0.12.25
cffi==1.16.0
clr-loader==0.2.6
proxy_tools==0.1.0
pycparser==2.22
pythonnet==3.0.3
pywebview==5.0.5
typing_extensions==4.11.0
</pre>

---

## Realice sus pruebas, actualizaciones o modificaciones.
Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

## Actualizar la receta.
Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```

---

## Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Realice pruebas de rutina.                    |  |
| Paso 8 | Finalice su gestión.                          | deactivate                            |

***
