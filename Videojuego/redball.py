import pygame
import random
import sys

class RedBall:
    def __init__(self, width, height):
        try:
            self.image = pygame.image.load('./assets/tank.png') # Carga la imagen del tanque
            # Escalar la imagen a un tamaño más pequeño 
            self.image = pygame.transform.scale(self.image, (50, 50)) # Escala la imagen a 50x50 píxeles
            self.rect = self.image.get_rect()  # Obtiene el rectángulo de la imagen
        except pygame.error as e:
            print(f"Error loading image: {e}") # Imprime un mensaje de error si la imagen no se puede cargar
            sys.exit(1) # Sale del programa si ocurre un error al cargar la imagen

        # Coloca la bola roja en una posición aleatoria dentro de los límites de la pantalla
        self.rect.x = random.randint(0, max(0, width - self.rect.width))
        self.rect.y = random.randint(0, max(0, height - self.rect.height))
        # Asigna una velocidad aleatoria en los ejes x e y
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def move(self, width, height):
        # Mueve la bola en base a su velocidad
        self.rect.x += self.speed_x # Mueve la bola en el eje x
        self.rect.y += self.speed_y # Mueve la bola en el eje y

        # Rebotar en los bordes de la pantalla
        if self.rect.x <= 0 or self.rect.x >= width - self.rect.width:
            self.speed_x *= -1 # Invierte la dirección horizontal
        if self.rect.y <= 0 or self.rect.y >= height - self.rect.height:
            self.speed_y *= -1 # Invierte la dirección vertical

    def draw(self, screen):
        # Dibuja la imagen del tanque en la pantalla en la posición actual
        screen.blit(self.image, self.rect.topleft)
