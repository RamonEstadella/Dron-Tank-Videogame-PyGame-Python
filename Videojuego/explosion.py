import pygame

class Explosion:

    '''
    INICIALIZACIÓN:

    En el constructor (__init__), cargamos las imágenes de explosión y las escalamos. 
    Almacenamos estas imágenes en una lista. También definimos el rectángulo de la imagen para posicionarla 
    correctamente y un contador para controlar la velocidad de la animación.

    '''
    def __init__(self, x, y):
        # Carga las imágenes de la explosión y las escala
        self.images = []
        for i in range(1, 4):  # Suponiendo que hay 3 imágenes de explosión (explosion1.png, explosion2.png, explosion3.png)
            img = pygame.image.load(f'assets/explosion{i}.png') # Carga la imagen de explosión
            img = pygame.transform.scale(img, (50, 50))  # Escala la imagen a 50x50 píxeles
            self.images.append(img) # Añade la imagen a la lista de imágenes de explosión
        self.index = 0 # Índice de la imagen actual
        self.image = self.images[self.index] # Imagen actual de la explosión
        self.rect = self.image.get_rect(center=(x, y)) # Define el rectángulo de la imagen en la posición (x, y)
        self.counter = 0 # Contador para controlar la velocidad de la animación
        self.finished = False # Bandera para indicar si la animación ha terminado

    '''
    MÉTODO DE ACTUALIZACIÓN

    El método update incrementa un contador en cada llamada. Cuando el contador alcanza un cierto valor 
    (que determina la velocidad de la animación), se avanza al siguiente frame de la animación. 
    Si la animación ha mostrado todas las imágenes, se marca como terminada.
    
    '''

    def update(self):
        explosion_speed = 5 # Velocidad de la animación (menor número = animación más rápida)
        self.counter += 1 # Incrementa el contador en cada actualización

        if self.counter >= explosion_speed: # Si el contador alcanza la velocidad de explosión
            self.counter = 0 # Reinicia el contador
            if self.index < len(self.images) - 1: # Si no es la última imagen de la secuencia
                self.index += 1  # Avanza al siguiente frame
                self.image = self.images[self.index] # Actualiza la imagen actual
            else:
                self.finished = True # Marca la animación como terminada

    '''
    MÉTODO DE DIBUJO

    El método draw dibuja la imagen actual de la explosión en la pantalla en la posición adecuada, 
    siempre que la animación no haya terminado.
    
    '''

    def draw(self, screen):
        if not self.finished: # Si la animación no ha terminado
            screen.blit(self.image, self.rect.topleft) # Dibuja la imagen actual en la pantalla en la posición correspondiente
