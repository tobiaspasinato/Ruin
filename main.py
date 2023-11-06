import pygame
from pygame.locals import *
from player import *
from constants import *

direccion = True

pygame.init() #Se inicializa pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("music_game.wav")
sonido_fondo.set_volume(VOLUMEN_MUSICA)
milis = pygame.time.Clock()
pygame.display.set_caption("Ruin") # Nombre de la pestaña
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana
running = True

lista_teclas = pygame.key.get_pressed()

while running:
    sonido_fondo.play()
    for event in pygame.event.get():# Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
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
            if lista_teclas[K_m]:
                sonido_fondo.stop()
                print("m")
            if lista_teclas[K_n]:
                sonido_fondo.stop()
                print("n")
    
    # milis(FPS)
    pygame.display.flip() # Muestra los cambios en la pantalla
    screen.fill((0, 0, 255))# Se pinta el fondo de la ventana
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)# Se dibuja un círculo azul en el centro
    pygame.display.flip()# Muestra los cambios en la pantalla
pygame.quit() # Fin