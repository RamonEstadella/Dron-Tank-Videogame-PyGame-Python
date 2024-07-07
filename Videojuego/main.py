import pygame
import sys
import math
from radar import Radar
from redball import RedBall
from button import Button
from explosion import Explosion

# Configuración inicial
pygame.init()  # Inicializa todos los módulos de Pygame
WIDTH, HEIGHT = 800, 600  # Define el ancho y alto de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Configura la ventana del juego
pygame.display.set_caption("Radar Militar") # Establece el título de la ventana

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Cargar y escalar la imagen de fondo
background_image = pygame.image.load('./assets/background.jpg')  # Carga la imagen de fondo
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT)) # Escala la imagen al tamaño de la ventana

def main():
    radar = Radar(WIDTH // 2, HEIGHT // 2, 100) # Crea una instancia de la clase Radar en el centro de la pantalla
    balls = [RedBall(WIDTH, HEIGHT) for _ in range(5)]  # Crear 5 bolas rojas
    button = Button(350, 500, 200, 50, "Shoot Missile") # Crea un botón con el texto "Shoot Missile"
    explosions = [] # Lista para almacenar las explosiones

    clock = pygame.time.Clock() # Inicializa el reloj para controlar la tasa de cuadros por segundo
    running = True # Bandera para mantener el juego corriendo
    game_over = False # Bandera para indicar si el juego ha terminado

    while running: # Bucle principal del juego
        for event in pygame.event.get(): # Manejo de eventos
            if event.type == pygame.QUIT: # Si se cierra la ventana
                pygame.quit() # Cierra Pygame
                sys.exit() # Sale del programa
            if not game_over and button.is_clicked(event): # Si el botón es clickeado y el juego no ha terminado
                for ball in balls: # Revisa cada bola roja
                    distance = math.sqrt((ball.rect.centerx - radar.x) ** 2 + (ball.rect.centery - radar.y) ** 2) # Calcula la distancia al radar
                    if distance < radar.radius: # Si la bola está dentro del radio del radar

                        '''CREAMOS EXPLOSIONES'''

                        explosions.append(Explosion(ball.rect.centerx, ball.rect.centery))  # Crea una explosión en la posición de la bola
                        balls.remove(ball) # Elimina la bola de la lista

        # Manejar entradas del teclado para mover la mira del radar
        keys = pygame.key.get_pressed() # Obtiene el estado de todas las teclas
        if keys[pygame.K_LEFT]: # Si la tecla izquierda está presionada
            radar.move(-5, 0) # Mueve el radar a la izquierda
        if keys[pygame.K_RIGHT]: # Si la tecla derecha está presionada
            radar.move(5, 0) # Mueve el radar a la derecha
        if keys[pygame.K_UP]: # Si la tecla arriba está presionada
            radar.move(0, -5) # Mueve el radar hacia arriba
        if keys[pygame.K_DOWN]: # Si la tecla abajo está presionada
            radar.move(0, 5) # Mueve el radar hacia abajo

        screen.blit(background_image, (0, 0))  # Dibujar la imagen de fondo en la pantalla
        radar.draw(screen) # Dibuja el radar en la pantalla

        
        if not game_over: # Si el juego no ha terminado
            for ball in balls: # Para cada bola roja
                ball.move(WIDTH, HEIGHT) # Mueve la bola
                ball.draw(screen) # Dibuja la bola en la pantalla

            '''ACTUALIZAMOS Y DIBUJAMOS EXPLOSIONES'''
            
            # Actualizar y dibujar explosiones
            for explosion in explosions: # Para cada explosión
                explosion.update() # Actualiza la animación de la explosión
                explosion.draw(screen) # Dibuja la explosión en la pantalla
            
            '''ELIMINAMOS EXPLOSIONES COMPLETADAS'''

            # Eliminar explosiones completadas
            explosions = [explosion for explosion in explosions if not explosion.finished] # Filtra las explosiones que han terminado

            button.draw(screen) # Dibuja el botón en la pantalla

            if not balls:  # Si no hay más tanques, establecer game_over a True
                game_over = True # Marca el juego como terminado

        if game_over: # Si el juego ha terminado
            font = pygame.font.SysFont(None, 75) # Crea una fuente para el texto de "GAME OVER"
            game_over_surface = font.render("GAME OVER", True, RED) # Renderiza el texto "GAME OVER"
            game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # Obtiene el rectángulo del texto
            screen.blit(game_over_surface, game_over_rect) # Dibuja el texto en el centro de la pantalla

        pygame.display.flip() # Actualiza la pantalla
        clock.tick(30) # Controla la tasa de cuadros por segundo a 30 FPS

if __name__ == "__main__":
    main() # Llama a la función principal del juego
