import pygame
from pygame.locals import *
from player import *
from constants import *

milis = pygame.time.Clock()

direccion = True

pygame.init() #Se inicializa pygame
pygame.display.set_caption("Ruin") # Nombre de la pestaña
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana
running = True
while running:
# Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        lista_teclas = pygame.key.get_pressed()
        if True in lista_teclas:
            if lista_teclas[K_a]:
                direccion = False
                print("a")
            if lista_teclas[K_s]:
                print("s")
            if lista_teclas[K_w]:
                print("w")
            if lista_teclas[K_d]:
                direccion = True
                print("d")
            if lista_teclas[K_l]:
                print("l")

screen.fill((255, 255, 255))# Se pinta el fondo de la ventana
# Se dibuja un círculo azul en el centro
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
pygame.display.flip()# Muestra los cambios en la pantalla
pygame.quit() # Fin