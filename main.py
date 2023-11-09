import pygame
from pygame.locals import *
from clases.player import *
from clases.enemy import *
from constants import *

direccion = True
milis = pygame.time.Clock()

pygame.init() #Se inicializa pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("music\music_game.wav")
sonido_fondo.set_volume(VOLUMEN_MUSICA)
pygame.display.set_caption("Ruin") # Nombre de la pestaña
imagen_backgrond = pygame.image.load("./imgs/level 1.png") # Cargar imagen del fondo
backgrond = pygame.transform.scale(imagen_backgrond, (LARGO_PANTALLA, ANCHO_PANTALLA))
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana

player1 = player()

running = True

while running:
    sonido_fondo.play()
    for event in pygame.event.get():# Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[K_a]:
            direccion = False
            player1.control(-5, 0)
        if lista_teclas[K_s]:
            player1.control(0, -5)
        if lista_teclas[K_w]:
            player1.control(0, 5)
        if lista_teclas[K_d]:
            direccion = True
            player1.control(5, 0)
        if lista_teclas[K_l]:
            print("l")
        if lista_teclas[K_m]:
            sonido_fondo.stop()
            print("m")
        if lista_teclas[K_n]:
            sonido_fondo.play()
            print("n")
    
    screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
    screen.blit(backgrond,(0,0)) # Ubicacion del fondo
    player1.upgrade()
    player1.dibujar(screen)
    pygame.display.flip()# Muestra los cambios en la pantalla
    milis.tick(FPS)
pygame.quit() # Fin