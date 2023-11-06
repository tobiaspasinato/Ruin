import pygame
from pygame.locals import *
from player import *
from constants import *

direccion = True
milis = pygame.time.Clock()

pygame.init() #Se inicializa pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("music\music_game.wav")
sonido_fondo.set_volume(VOLUMEN_MUSICA)
pygame.display.set_caption("Ruin") # Nombre de la pestaña
imagen_backgrond = pygame.image.load("./imgs/fondo_game.png") # Cargar imagen del fondo
backgrond = pygame.transform.scale(imagen_backgrond, (LARGO_PANTALLA, ANCHO_PANTALLA))
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana
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
            sonido_fondo.play()
            print("n")
    
    screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
    screen.blit(backgrond,(0,0)) # Ubicacion del fondo
    pygame.display.flip()# Muestra los cambios en la pantalla
    milis(FPS)
pygame.quit() # Fin