# gestionador_dinamico
Gestionador dinámico de repositorios

El presente script permite navegar de forma eficiente un listado de repositorios, 
con la finalidad de hacer una gestión en particular en ellos, de una forma rápida y cómoda, 
priorizando el orden.

Esta presente en el directorio de este documento un archivo llamado: gestion_microservicios.txt

Es una tabla donde se visualizan tres columnas separadas por “|”

La primera columna hace referencia al nombre del proyecto.

La segunda columna hace referencia a la gestión realizada.

La tercera columna hace referencia a la URL a ser gestionada.

El presente programa lo que hace es recorrer uno a uno los registros,
Abrir la url asignada a traves de un navegador propio construido por python.
Esto es ejecutando el archivo main.py

El desarrollador hará en dicho sitio web la operación que le corresponda realizar.
Luego de ello, cerrará la ventana del navegador que fue construido por python.
Y automaticamente, en la consola se preguntara si la gestión ha sido realizada satisfactoriamente, o si se debe realizar de nuevo mas adelante, esto es 1 para ya gestionado y 0 para no gestionado.

Dada la respuesta, luego de presionar Enter, automáticamente se abrirá la ventana de navegación web con la URL asignada al siguiente registro. De esta manera, se irán gestionando todas las URL del listado.

Al finalizar la ejecución del programa el listado de las URL en gestion_microservicios.txt será actualizado, de manera que al ejecutar de nuevo el programa, se gestionarán solo las URL que faltan por trabajar.

Este Script me permitió gestionar de forma rápida y eficiente las vulnerabilidades fluid que hacían referencia a problemas de seguridad en Dockerfile en más de 28 proyectos en tan solo un día de trabajo, así como los cambios masivos que se presentarán durante mi gestión.

Espero que este aporte sea de utilidad.

Óscar Iván González Peña
Consultor de Desarrollo
To. ADSI SENA
