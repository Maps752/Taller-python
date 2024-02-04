import pygame
import time

pygame.init()

size = width, height = 200, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simulación de Semáforo")

# Definición de colores
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def draw_traffic_light(color):
    screen.fill(BLACK)  # Fondo negro
    if color == 'red':
        pygame.draw.circle(screen, RED, (100, 150), 50)
    elif color == 'yellow':
        pygame.draw.circle(screen, YELLOW, (100, 300), 50)
    elif color == 'green':
        pygame.draw.circle(screen, GREEN, (100, 450), 50)
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_traffic_light('red')
    time.sleep(2)  # Espera 2 segundos
    draw_traffic_light('yellow')
    time.sleep(2)  # Espera 2 segundos
    draw_traffic_light('green')
    time.sleep(2)  # Espera 3 segundos
    running=False #Salir del semaforo

pygame.quit()
