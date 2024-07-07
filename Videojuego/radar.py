import pygame

BLACK = (0, 0, 0)

class Radar:
    def __init__(self, x, y, radius):
        # Inicializa las coordenadas (x, y) del radar y su radio
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        # Dibuja el círculo del radar
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius, 2)
        # Dibuja las líneas de mira del radar
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x, self.y - self.radius), 2)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + self.radius, self.y), 2)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x, self.y + self.radius), 2)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x - self.radius, self.y), 2)

    def move(self, dx, dy):
        # Mueve el radar sumando las diferencias (dx, dy) a las coordenadas actuales
        self.x += dx
        self.y += dy

    
