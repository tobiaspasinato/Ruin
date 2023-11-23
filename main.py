import pygame
from pygame.locals import *
from clases.player import player
from clases.enemy import enemy
from clases.coin import coin
from clases.bandera import bandera
from constants import *

direccion = True
score = 0
level1 = True
level2 = False
level3 = False
milis = pygame.time.Clock()

pygame.init() #Se inicializa pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("music\music_game.wav")
sonido_fondo.set_volume(VOLUMEN_MUSICA)
font = pygame.font.SysFont("Arial Narrow", 50)
text_score = font.render(f"Score: {score}", True, (0, 0, 0))
pygame.display.set_caption("Ruin") # Nombre de la pestaña
imagen_level1 = pygame.image.load("./imgs/level 1.png") # Cargar imagen del fondo
level1_img = pygame.transform.scale(imagen_level1, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_level2 = pygame.image.load("./imgs/level 2.png") # Cargar imagen del fondo
level2_img = pygame.transform.scale(imagen_level2, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_level3 = pygame.image.load("./imgs/level 3.png") # Cargar imagen del fondo
level3_img = pygame.transform.scale(imagen_level3, (LARGO_PANTALLA, ANCHO_PANTALLA))
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana

if level1 == True:
    flag_coin1 = False
    player1 = player(175, 0)
    # enemy1 = enemy(250, 250)
    coin1 = coin(200, 200)
    bandera1 = bandera(150, 300)
elif level2 == True:
    flag_coin2 = False
    player2 = player(175, 0)
    # enemy1 = enemy(250, 250)
    coin2 = coin(200, 200)
    bandera2 = bandera(150, 300)
elif level3 == True:
    flag_coin3 = False
    player3 = player(175, 0)
    # enemy1 = enemy(250, 250)
    coin3 = coin(200, 200)
    bandera3 = bandera(150, 300)

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
        if lista_teclas[K_m]:
            sonido_fondo.stop()
    
    text_score = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
    if level1 == True:
        screen.blit(level1_img,(0,0)) # Ubicacion del fondo
    elif level2 == True:
        screen.blit(level2_img,(0,0)) # Ubicacion del fondo
    elif level3 == True:
                screen.blit(level3_img,(0,0)) # Ubicacion del fondo
    screen.blit(text_score,(350,10))
    # enemy1.moves()
    # enemy1.upgrade()
    # enemy1.dibujar(screen)
    if flag_coin1 == False:
        coin1.upgrade()
        coin1.dibujar(screen)
        if player1.rect.colliderect(coin1.rect):
            flag_coin1 = True
            score = score + 10
    if flag_coin1 == True:
        bandera1.upgrade()
        bandera1.dibujar(screen)
        if player1.rect.colliderect(bandera1.rect):
            level1 = False
            level2 = True
            level3 = False
    player1.upgrade()
    player1.dibujar(screen, accion_personaje, direccion)
    pygame.display.flip()# Muestra los cambios en la pantalla
    milis.tick(FPS)
pygame.quit() # Fin