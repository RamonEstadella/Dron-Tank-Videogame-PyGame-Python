# Planteamiento Previo

*Objetivo:*

Crear una animación de explosión que se pueda mostrar en el juego cuando se necesite, como al colisionar un objeto o al disparar un misil.

*Requisitos*

- Necesitamos una serie de imágenes que representan diferentes etapas de una explosión.
- La animación debe reproducirse secuencialmente y detenerse al final.
- La explosión debe aparecer en una posición específica en la pantalla.
- El código debe ser capaz de actualizar la animación y dibujarla en la pantalla.

*Recopilación de Recursos*

Tres imágenes de explosión nombradas de manera secuencial (e.g., explosion1.png, explosion2.png, explosion3.png).
Biblioteca Pygame para manejar gráficos y eventos.

*Diseño de la Clase Explosion*

La clase debe ser capaz de:

- Cargar y almacenar las imágenes de la explosión.
- Escalar las imágenes a un tamaño manejable.
- Actualizar la animación cambiando las imágenes a lo largo del tiempo.
- Dibujar la imagen actual de la explosión en la pantalla.

*Metodología*

- Inicialización: En el constructor, cargar todas las imágenes y configurarlas en la posición deseada.

- Actualización: Implementar un método update que avance la animación frame por frame.

- Dibujo: Implementar un método draw para dibujar la imagen actual en la pantalla.

# Desarrollo del Código

*Inicialización*

En el constructor (__init__), cargamos las imágenes de explosión y las escalamos. Almacenamos estas imágenes en una lista. También definimos el rectángulo de la imagen para posicionarla correctamente y un contador para controlar la velocidad de la animación.

*Método de Actualización*

El método update incrementa un contador en cada llamada. Cuando el contador alcanza un cierto valor (que determina la velocidad de la animación), se avanza al siguiente frame de la animación. Si la animación ha mostrado todas las imágenes, se marca como terminada.

*Método de Dibujo*

El método draw dibuja la imagen actual de la explosión en la pantalla en la posición adecuada, siempre que la animación no haya terminado.