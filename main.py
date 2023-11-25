import pygame
from pygame.locals import *
from clases.player import player
from clases.enemy import enemy
from clases.coin import coin
from clases.bandera import bandera
from clases.muro import muro
from constants import *

direccion = True
score = 0
segundos = 0
level1 = True
level2 = False
level3 = False
player_level1 = True
player_level2 = False
player_level3 = False
flag_coin1 = False
flag_coin2 = False
flag_coin3 = False
fin_timer = False
win_flag = False

milis = pygame.time.Clock()

pygame.init() #Se inicializa pygame
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("music\music_game.wav")
sonido_fondo.set_volume(VOLUMEN_MUSICA)
font = pygame.font.SysFont("Arial Narrow", 50)
text_score = font.render(f"Score: {score}", True, (0, 0, 0))
text_time = font.render(f"Time: {segundos}", True, (0, 0, 0))
text_restart = font.render("Restart", True, (255, 255, 255))
pygame.display.set_caption("Ruin") # Nombre de la pestaña
imagen_level1 = pygame.image.load("./imgs/level 1.png") # Cargar imagen del fondo
level1_img = pygame.transform.scale(imagen_level1, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_level2 = pygame.image.load("./imgs/level 2.png") # Cargar imagen del fondo
level2_img = pygame.transform.scale(imagen_level2, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_level3 = pygame.image.load("./imgs/level 3.png") # Cargar imagen del fondo
level3_img = pygame.transform.scale(imagen_level3, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_ganar = pygame.image.load("imgs\end_img.png") # Cargar imagen del fondo
win_img = pygame.transform.scale(imagen_ganar, (LARGO_PANTALLA, ANCHO_PANTALLA))
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana

player1 = player(0, 0)
pared0_level1 = muro(0, 0, 500, 1)
pared01_level1 = muro(0, 0, 1, 500)
pared02_level1 = muro(0, 499, 500, 1)
pared03_level1 = muro(499, 0, 1, 500)
#level 1
pared1_level1 = muro(405, 0, 95, 500)
pared2_level1 = muro(0, 0, 40, 135)
pared3_level1 = muro(0, 139, 1, 140)
coin1 = coin(335, 298)
bandera1 = bandera(55, 470)
coin2 = coin(125, 340)
bandera2 = bandera(255, 5)
coin3 = coin(100, 175)
bandera3 = bandera(250, 220)

running = True

while running:
    accion_personaje = "stay"
    sonido_fondo.play()
    for event in pygame.event.get():# Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos
            print(mouse)
            if win_flag == True:
                if (mouse[0] > 0 and mouse[0] < 140) and (mouse[1] < 500 and mouse[1] > 440):
                    direccion = True
                    score = 0
                    segundos = 0
                    level1 = True
                    level2 = False
                    level3 = False
                    player_level1 = True
                    player_level2 = False
                    player_level3 = False
                    flag_coin1 = False
                    flag_coin2 = False
                    flag_coin3 = False
                    fin_timer = False
                    win_flag = False
        if event.type == timer_segundos:
            if fin_timer == False:
                segundos = segundos + 1
    if win_flag == False:
        lista_teclas = pygame.key.get_pressed()
        if True in lista_teclas:
            if lista_teclas[K_a]:
                direccion = False
                accion_personaje = "walk"
                player1.control(-3, 0)
            if lista_teclas[K_s]:
                accion_personaje = "walk"
                player1.control(0, 3)
            if lista_teclas[K_w]:
                accion_personaje = "walk"
                player1.control(0, -3)
            if lista_teclas[K_d]:
                direccion = True
                accion_personaje = "walk"
                player1.control(3, 0)
            if lista_teclas[K_m]:
                sonido_fondo.stop()
        
        text_score = font.render(f"Score: {score}", True, (0, 0, 0))
        text_time = font.render(f"Time: {segundos}", True, (0, 0, 0))
        screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
        if level1 == True:
            pared1_level1.crear_muro(screen)
            pared2_level1.crear_muro(screen)
            pared0_level1.crear_muro(screen)
            pared01_level1.crear_muro(screen)
            pared02_level1.crear_muro(screen)
            pared03_level1.crear_muro(screen)
            screen.blit(level1_img,(0,0)) # Ubicacion del fondo
            # pared3_level1.crear_muro(screen)
        elif level2 == True:
            pared0_level1.crear_muro(screen)
            pared01_level1.crear_muro(screen)
            pared02_level1.crear_muro(screen)
            pared03_level1.crear_muro(screen)
            screen.blit(level2_img,(0,0)) # Ubicacion del fondo
        elif level3 == True:
            pared0_level1.crear_muro(screen)
            pared01_level1.crear_muro(screen)
            pared02_level1.crear_muro(screen)
            pared03_level1.crear_muro(screen)
            screen.blit(level3_img,(0,0)) # Ubicacion del fondo
        if level1 == True:
            if player1.rect.colliderect(pared02_level1.rect):
                player1.control(0, -3)
            if player1.rect.colliderect(pared01_level1.rect):
                player1.control(3, 0)
            if player1.rect.colliderect(pared0_level1.rect):
                player1.control(0, 3)
            if player1.rect.colliderect(pared1_level1.rect):
                player1.control(-3, 0)
            if player1.rect.colliderect(pared2_level1.rect):
                player1.control(3, 0)
            # if player1.rect.colliderect(pared3_level1.rect):
            #     player1.control(0, -3)
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
        if level2 == True:
            if player1.rect.colliderect(pared03_level1.rect):
                player1.control(-3, 0)
            if player1.rect.colliderect(pared02_level1.rect):
                player1.control(0, -3)
            if player1.rect.colliderect(pared01_level1.rect):
                player1.control(3, 0)
            if player1.rect.colliderect(pared0_level1.rect):
                player1.control(0, 3)
            if flag_coin2 == False:
                coin2.upgrade()
                coin2.dibujar(screen)
                if player1.rect.colliderect(coin2.rect):
                    flag_coin2 = True
                    score = score + 10
            if flag_coin2 == True:
                bandera2.upgrade()
                bandera2.dibujar(screen)
                if player1.rect.colliderect(bandera2.rect):
                    level1 = False
                    level2 = False
                    level3 = True
        if level3 == True:
            if player1.rect.colliderect(pared03_level1.rect):
                player1.control(-3, 0)
            if player1.rect.colliderect(pared02_level1.rect):
                player1.control(0, -3)
            if player1.rect.colliderect(pared01_level1.rect):
                player1.control(3, 0)
            if player1.rect.colliderect(pared0_level1.rect):
                player1.control(0, 3)
            if flag_coin3 == False:
                coin3.upgrade()
                coin3.dibujar(screen)
                if player1.rect.colliderect(coin3.rect):
                    flag_coin3 = True
                    score = score + 10
            if flag_coin3 == True:
                bandera3.upgrade()
                bandera3.dibujar(screen)
                if player1.rect.colliderect(bandera3.rect):
                    level1 = False
                    level2 = False
                    level3 = False
                    fin_timer = True
                    win_flag = True
        player1.upgrade()
        player1.dibujar(screen, accion_personaje, direccion)
        screen.blit(text_score,(325,10))
        screen.blit(text_time,(10,10))
    if win_flag == True:
        screen.blit(win_img,(0,0)) # Ubicacion del fondo
        screen.blit(text_restart,(10,450))
    pygame.display.flip()# Muestra los cambios en la pantalla
    milis.tick(FPS)
pygame.quit() # Fin

"""
falta poner las paredes
"""