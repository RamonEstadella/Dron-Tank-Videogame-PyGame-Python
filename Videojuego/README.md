*SIMULACIÓN DE UN DRON MILITAR ANTI-TANQUE*

**Creado por: Ramon Estadella Serra**

## Descripción
Este proyecto es un videojuego senzillo creado con la libreria de Python, PyGame.
Forma parte de una actividad de entrega del Curso Especialista en Python 2024 de la Universidad Internacional de Valencia (VIU).

Este proyecto consiste en un videojuego que simula una vista aérea de Dron Militar que dispara misiles aire-tierra a una división de tanques en terreno de combate.

Para conseguir esto, se han utilizado animaciones de explosión usando varias imágenes que representan un proceso de explosión. Cuando el objetivo, el tanque enemigo, pasa por dentro de el punto de mira del Dron Militar, al pulsar el botón de disparar mísil (Shoot Missile) se elimina el tanque enemigo. 
Se deben eliminar todos los tanques para terminar el juego. Se muestra un "Game Over" cuando 
todos los tanques enemigos han sigo eliminados. Después, para salir del juego se debe pulsar a la cruz de cerrar pestaña o ventana, saliendo del bucle del juego.

Primeramente, se programaron bolitas rojas en vez de tanques de combate, y al pasar por el punto de mira del dron, si se pulsaba el botón de "disparar mísil", se eliminavan las bolitas rojas.

Con el fin de crear un videojuego más realista y divertido, se han substituido las bolitas rojas por imagenes/siluetas aéreas de tanques de combate.
La imagen de fondo de la ventana del videojuego representa un terreno de combate sacado de UnSplash, la web sin fotos con CopyRight de libre descarga.

Los tanques enemigos primeramente no estaban a escala de la ventana del videojuego, por lo que se ha tenido que añadir código en "redball.py" para disminuir su tamaño de imagen.

También se ha escalado la imagen de "background" que simula el terreno de combate con el fin de que ocupe todo el tamaño de ventana del videojuego.

Se ha añadido código para que los tanques enemigos reboten al tocar con el límite de pantalla,
así se hace posible que pasen por el punto de mira del dron militar y puedan ser eliminados por el usuario.

Todas las imágenes se encuentran en el directorio "assets", y son usadas e importadas por el código Python por cada una de sus utilidades y funciones.

Para termianr, el código sigue un paradigma de Programación Orientada a Objetos, así modularizamos el código del proyecto, se hace más fácil su comprensión, estructura, escalabilidad, etc.



## Uso y Ejecución
El videojuego debe inicializarse mediante el comando de terminal "python main.py", así se ejecuta la clase "main.py" que contiene la información y código principal del proyecto. 

"main.py" importa las diferentes clases que representan los diferentes elementos del proyecto del videojuego: RADAR, REDBALL(los tanques enemigos), BUTTON (el botón de disparar), y EXPLOSION (que representa la explosión al impactar el mísil en el tanque enemigo).

