import pygame
from pygame.locals import *
from clases.player import *
from clases.enemy import *
from constants import *

direccion = True
score = 0
milis = pygame.time.Clock()

pygame.init() #Se inicializa pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("music\music_game.wav")
sonido_fondo.set_volume(VOLUMEN_MUSICA)
font = pygame.font.SysFont("Arial Narrow", 50)
text_score = font.render(f"Score: {score}", True, (0, 0, 0))
pygame.display.set_caption("Ruin") # Nombre de la pestaña
imagen_backgrond = pygame.image.load("./imgs/level 1.png") # Cargar imagen del fondo
backgrond = pygame.transform.scale(imagen_backgrond, (LARGO_PANTALLA, ANCHO_PANTALLA))
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana

player1 = player(175, 0)
enemy1 = enemy(140, 100)

running = True

while running:
    accion_personaje = "stay"
    sonido_fondo.play()
    for event in pygame.event.get():# Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[K_a]:
            direccion = False
            accion_personaje = "walk"
            player1.control(-2, 0)
        if lista_teclas[K_s]:
            accion_personaje = "walk"
            player1.control(0, 2)
        if lista_teclas[K_w]:
            accion_personaje = "walk"
            player1.control(0, -2)
        if lista_teclas[K_d]:
            direccion = True
            accion_personaje = "walk"
            player1.control(2, 0)
        if lista_teclas[K_l]:
            accion_personaje = "atack"
        if lista_teclas[K_m]:
            sonido_fondo.stop()
    text_score = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
    screen.blit(backgrond,(0,0)) # Ubicacion del fondo
    screen.blit(text_score,(350,10))
    enemy1.moves()
    enemy1.upgrade()
    enemy1.dibujar(screen)
    player1.upgrade()
    player1.dibujar(screen, accion_personaje, direccion)
    pygame.display.flip()# Muestra los cambios en la pantalla
    milis.tick(FPS)
pygame.quit() # Fin