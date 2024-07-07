import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x # Coordenada x del botón
        self.y = y # Coordenada y del botón
        self.width = width # Ancho del botón
        self.height = height # Alto del botón
        self.text = text # Texto del botón
        self.rect = pygame.Rect(x, y, width, height)  # Define el rectángulo del botón
        self.clicked = False # Bandera para saber si el botón ha sido clickeado

    def draw(self, screen):
        # Dibuja el rectángulo del botón
        pygame.draw.rect(screen, WHITE, self.rect)
        # Crea la fuente para el texto
        font = pygame.font.SysFont(None, 40)
        # Renderiza el texto
        text_surface = font.render(self.text, True, BLACK)
        # Obtiene el rectángulo del texto y lo centra en el botón
        text_rect = text_surface.get_rect(center=self.rect.center)
        # Dibuja el texto en la pantalla
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        # Verifica si el evento es un click del mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Verifica si la posición del click está dentro del rectángulo del botón
            if self.rect.collidepoint(event.pos):
                self.clicked = True # Marca el botón como clickeado
                return True # Devuelve True si el botón ha sido clickeado
        return False  # Devuelve False si el botón no ha sido clickeado
