import pygame
from constants import *

pygame.init() #Se inicializa pygame
pygame.display.set_caption("Ruin") # Nombre de la pestaña
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana
running = True
while running:
# Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((255, 255, 255))# Se pinta el fondo de la ventana
# Se dibuja un círculo azul en el centro
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
pygame.display.flip()# Muestra los cambios en la pantalla
pygame.quit() # Fin