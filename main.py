import pygame
import re
from pygame.locals import *
from clases.player import player
from clases.enemy import enemy
from clases.coin import coin
from clases.bandera import bandera
from clases.muro import muro
from constants import *
from function import *

menu_flag = True
game_over_flag = False
score_flag = False

direccion = True
direccion_enemy = True
aparicion_level1 = True
aparicion_level2 = False #False
aparicion_level3 = False #False
score = 0
segundos = 0
level1 = True  #true
level2 = False #false
level3 = False #false
flag_coin1 = False
flag_coin2 = False
flag_coin3 = False
fin_timer = True
win_flag = False
usuario = []

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
text_save = font.render("Save", True, (255, 255, 255))
text_menu = font.render("Menu", True, (255, 255, 255))
pygame.display.set_caption("Ruin") # Nombre de la pestaña
imagen_level1 = pygame.image.load("./imgs/level 1.png") # Cargar imagen del fondo
level1_img = pygame.transform.scale(imagen_level1, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_level2 = pygame.image.load("./imgs/level 2.png") # Cargar imagen del fondo
level2_img = pygame.transform.scale(imagen_level2, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_level3 = pygame.image.load("./imgs/level 3.png") # Cargar imagen del fondo
level3_img = pygame.transform.scale(imagen_level3, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_ganar = pygame.image.load("imgs\end_img.png") # Cargar imagen del fondo
win_img = pygame.transform.scale(imagen_ganar, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_menu = pygame.image.load("imgs\\fondo_game.png") # Cargar imagen del fondo
menu_img = pygame.transform.scale(imagen_menu, (LARGO_PANTALLA, ANCHO_PANTALLA))
imagen_score1122 = pygame.image.load("imgs\\score_table.png")
score_img1122 = pygame.transform.scale(imagen_score1122, (LARGO_PANTALLA, ANCHO_PANTALLA))
screen = pygame.display.set_mode([LARGO_PANTALLA, ANCHO_PANTALLA]) #Se crea una ventana

player1 = player(0, 0)
enemy1 = enemy(0, 0)
enemy2 = enemy(0, 0)
pared0_level1 = muro(0, 0, 500, 1)
pared01_level1 = muro(0, 0, 1, 500)
pared02_level1 = muro(0, 499, 500, 1)
pared03_level1 = muro(499, 0, 1, 500)
#level 1
pared1_level1 = muro(405, 0, 1, 500)
pared2_level1 = muro(40, 0, 1, 130)
pared3_level1 = muro(0, 130, 39, 1)
pared4_level1 = muro(215, 130, 190, 1)
pared5_level1 = muro(215, 132, 1, 70)
pared6_level1 = muro(217, 205, 190, 1)
pared7_level1 = muro(95, 390, 400, 1)
pared8_level1 = muro(95, 392, 1, 110)
pared9_level1 = muro(0, 395, 35, 1)
pared10_level1 = muro(35, 401, 1, 100)
#level 2
pared1_level2 = muro(0, 395, 500, 1)
pared2_level2 = muro(95, 0, 1, 500)
pared3_level2 = muro(404, 0, 1, 140)
pared4_level2 = muro(407, 138, 100, 1)
pared5_level2 = muro(0, 180, 210, 1)
pared6_level2 = muro(0, 70, 210, 1)
pared7_level2 = muro(213, 70, 1, 110)
pared8_level2 = muro(253, 230, 60, 1)
pared9_level2 = muro(253, 300, 60, 1)
pared10_level2 = muro(251, 230, 1, 72)
pared11_level2 = muro(314, 233, 1, 67)
#level 3
pared1_level3 = muro(95, 0, 1, 500)
pared2_level3 = muro(430, 0, 1, 500)
pared3_level3 = muro(0, 150, 500, 1)
pared4_level3 = muro(275, 300, 225, 1)
pared5_level3 = muro(273, 302, 1, 128)
pared6_level3 = muro(275, 430, 225, 1)
pared7_level3 = muro(155, 370, 65, 1)
pared8_level3 = muro(155, 440, 65, 1)
pared9_level3 = muro(155, 372, 1, 62)
pared10_level3 = muro(220, 372, 1, 62)

coin1 = coin(335, 298)
bandera1 = bandera(55, 470)
coin2 = coin(125, 340)
bandera2 = bandera(255, 5)
coin3 = coin(100, 175)
bandera3 = bandera(250, 220)

running = True

while running:
    #sonido_fondo.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos
            if menu_flag == True:
                if (mouse[0] > 175 and mouse[0] < 330) and (mouse[1] < 380 and mouse[1] > 280):
                    menu_flag = False
                if (mouse[0] > 0 and mouse[0] < 75) and (mouse[1] < 500 and mouse[1] > 420):
                    print("holii")
                    menu_flag = False
                    score_flag = True
            if score_flag == True:
                if (mouse[0] > 425 and mouse[0] < 500) and (mouse[1] < 500 and mouse[1] > 420):
                    print("holiiiiasd")
                    score_flag = False
                    menu_flag = True
            if game_over_flag == True:
                if (mouse[0] > 0 and mouse[0] < 140) and (mouse[1] < 500 and mouse[1] > 440):
                    direccion = True
                    direccion_enemy = True
                    aparicion_level1 = True
                    aparicion_level2 = False #False
                    aparicion_level3 = False #False
                    score = 0
                    segundos = 0
                    level1 = True  #true
                    level2 = False #false
                    level3 = False #false
                    flag_coin1 = False
                    flag_coin2 = False
                    flag_coin3 = False
                    fin_timer = False
                    win_flag = False
                    game_over_flag = False
                if (mouse[0] > 380 and mouse[0] < 500) and (mouse[1] < 500 and mouse[1] > 440):
                    menu_flag = True
                    direccion = True
                    direccion_enemy = True
                    aparicion_level1 = True
                    aparicion_level2 = False #False
                    aparicion_level3 = False #False
                    score = 0
                    segundos = 0
                    level1 = True  #trued
                    level2 = False #false
                    level3 = False #false
                    flag_coin1 = False
                    flag_coin2 = False
                    flag_coin3 = False
                    fin_timer = False
                    win_flag = False
                    game_over_flag = False
                if win_flag == True:
                    if (mouse[0] > 200 and mouse[0] < 300) and (mouse[1] < 500 and mouse[1] > 440):
                        guardar_archivo("tiempo.csv", f"{nuevo_usuario}\n")
        if event.type == timer_segundos:
                if fin_timer == False:
                    segundos += 1
    if menu_flag == True:
        screen.blit(menu_img,(0,0))
    elif menu_flag == False:
        if score_flag == True:
            lista_scores = []
            y = 200
            screen.blit(score_img1122,(0,0))
            lista_scores = leer_score_csv("tiempo.csv", lista_scores)
            # print(lista_scores)
            for elemento in lista_scores:
                nombre = elemento["nombre"]
                segundos_xs = elemento['segundos']
                mostrar_texto(font, screen, nombre, BLANCO, 100,y)
                mostrar_texto(font, screen, segundos_xs , BLANCO, 300,y)
                y += 50
        elif score_flag == False:
            fin_timer = False
            accion_personaje = "stay"
            if game_over_flag == False:
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
                    screen.blit(level1_img,(0,0)) # Ubicacion del fondo
                    pared1_level1.crear_muro(screen)
                    pared2_level1.crear_muro(screen)
                    pared0_level1.crear_muro(screen)
                    pared01_level1.crear_muro(screen)
                    pared02_level1.crear_muro(screen)
                    pared03_level1.crear_muro(screen)
                    pared3_level1.crear_muro(screen)
                    pared4_level1.crear_muro(screen)
                    pared5_level1.crear_muro(screen)
                    pared6_level1.crear_muro(screen)
                    pared7_level1.crear_muro(screen)
                    pared8_level1.crear_muro(screen)
                    pared9_level1.crear_muro(screen)
                    pared10_level1.crear_muro(screen)
                    #screen.blit(level1_img,(0,0)) # Ubicacion del fondo
                elif level2 == True:
                    pared0_level1.crear_muro(screen)
                    pared01_level1.crear_muro(screen)
                    pared02_level1.crear_muro(screen)
                    pared03_level1.crear_muro(screen)
                    pared1_level2.crear_muro(screen)
                    pared2_level2.crear_muro(screen)
                    pared3_level2.crear_muro(screen)
                    pared4_level2.crear_muro(screen)
                    pared5_level2.crear_muro(screen)
                    pared6_level2.crear_muro(screen)
                    pared7_level2.crear_muro(screen)
                    pared8_level2.crear_muro(screen)
                    pared9_level2.crear_muro(screen)
                    pared10_level2.crear_muro(screen)
                    pared11_level2.crear_muro(screen)
                    screen.blit(level2_img,(0,0)) # Ubicacion del fondo
                elif level3 == True:
                    pared0_level1.crear_muro(screen)
                    pared01_level1.crear_muro(screen)
                    pared02_level1.crear_muro(screen)
                    pared03_level1.crear_muro(screen)
                    pared1_level3.crear_muro(screen)
                    pared2_level3.crear_muro(screen)
                    pared3_level3.crear_muro(screen)
                    pared4_level3.crear_muro(screen)
                    pared5_level3.crear_muro(screen)
                    pared6_level3.crear_muro(screen)
                    pared7_level3.crear_muro(screen)
                    pared8_level3.crear_muro(screen)
                    pared9_level3.crear_muro(screen)
                    pared10_level3.crear_muro(screen)
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
                    if player1.rect.colliderect(pared3_level1.rect):
                        player1.control(0, 3)
                    if player1.rect.colliderect(pared4_level1.rect):
                        player1.control(0, -3)
                    if player1.rect.colliderect(pared5_level1.rect):
                        player1.control(-3, 0)
                    if player1.rect.colliderect(pared6_level1.rect):
                        player1.control(0, 3)
                    if player1.rect.colliderect(pared7_level1.rect):
                        player1.control(0, -3)
                    if player1.rect.colliderect(pared8_level1.rect):
                        player1.control(-3, 0) #d
                    if player1.rect.colliderect(pared9_level1.rect):
                        player1.control(0, -3) #s
                    if player1.rect.colliderect(pared10_level1.rect):
                        player1.control(3, 0) #a
                    if enemy1.rect.colliderect(pared6_level1):
                        direccion_enemy = False
                    if enemy1.rect.colliderect(pared7_level1):
                        direccion_enemy = True
                    if aparicion_level1 == True:
                        player1.rect.x = 170
                        player1.rect.y= 1
                        enemy1.rect.x = 230
                        enemy1.rect.y= 250
                        aparicion_level1 = False
                        aparicion_level2 = True
                    enemy1.moves(direccion_enemy)
                    enemy1.upgrade()
                    enemy1.dibujar(screen)
                    if player1.rect.colliderect(enemy1.rect):
                        game_over_flag = True
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
                    if player1.rect.colliderect(pared1_level2.rect):
                        player1.control(0, -3) #s
                    if player1.rect.colliderect(pared2_level2.rect):
                        player1.control(3, 0) #a
                    if player1.rect.colliderect(pared3_level2.rect):
                        player1.control(-3, 0) #d
                    if player1.rect.colliderect(pared4_level2.rect):
                        player1.control(0, 3) # w
                    if player1.rect.colliderect(pared5_level2.rect):
                        player1.control(0, 3) # w
                    if player1.rect.colliderect(pared6_level2.rect):
                        player1.control(0, -3) #s
                    if player1.rect.colliderect(pared7_level2.rect):
                        player1.control(3, 0) #a
                    if player1.rect.colliderect(pared8_level2.rect):
                        player1.control(0, -3) #s
                    if player1.rect.colliderect(pared9_level2.rect):
                        player1.control(0, 3) # w
                    if player1.rect.colliderect(pared10_level2.rect):
                        player1.control(-3, 0) #d
                    if player1.rect.colliderect(pared11_level2.rect):
                        player1.control(3, 0) #a
                    if enemy1.rect.colliderect(pared5_level2):
                        direccion_enemy = False
                    if enemy1.rect.colliderect(pared1_level2):
                        direccion_enemy = True
                    if flag_coin2 == False:
                        coin2.upgrade()
                        coin2.dibujar(screen)
                        if player1.rect.colliderect(coin2.rect):
                            flag_coin2 = True
                            score = score + 10
                    if aparicion_level2 == True:
                        player1.rect.x = 450
                        player1.rect.y= 300
                        enemy1.rect.x = 185
                        enemy1.rect.y= 280
                        enemy2.rect.x = 285
                        enemy2.rect.y= 100
                        aparicion_level2 = False
                        aparicion_level3 = True
                    enemy1.moves(direccion_enemy)
                    enemy1.upgrade()
                    enemy1.dibujar(screen)
                    enemy2.moves_x(direccion_enemy)
                    enemy2.upgrade()
                    enemy2.dibujar(screen)
                    if player1.rect.colliderect(enemy1.rect):
                        game_over_flag = True
                    if player1.rect.colliderect(enemy2.rect):
                        game_over_flag = True
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
                    if player1.rect.colliderect(pared1_level3.rect):
                        player1.control(3, 0) #a
                    if player1.rect.colliderect(pared2_level3.rect):
                        player1.control(-3, 0) #d
                    if player1.rect.colliderect(pared3_level3.rect):
                        player1.control(0, 3) # w
                    if player1.rect.colliderect(pared4_level3.rect):
                        player1.control(0, -3) #s
                    if player1.rect.colliderect(pared5_level3.rect):
                        player1.control(-3, 0) #d
                    if player1.rect.colliderect(pared6_level3.rect):
                        player1.control(0, 3) # w
                    if player1.rect.colliderect(pared7_level3.rect):
                        player1.control(0, -3) #s
                    if player1.rect.colliderect(pared8_level3.rect):
                        player1.control(0, 3) # w
                    if player1.rect.colliderect(pared9_level3.rect):
                        player1.control(-3, 0) #d
                    if player1.rect.colliderect(pared10_level3.rect):
                        player1.control(3, 0) #a
                    if enemy2.rect.colliderect(pared1_level3):
                        direccion_enemy = False
                    if enemy2.rect.colliderect(pared2_level3):
                        direccion_enemy = True
                    if flag_coin3 == False:
                        coin3.upgrade()
                        coin3.dibujar(screen)
                        if player1.rect.colliderect(coin3.rect):
                            flag_coin3 = True
                            score = score + 10
                    if aparicion_level3 == True:
                        player1.rect.x = 250
                        player1.rect.y= 445
                        enemy2.rect.x = 250
                        enemy2.rect.y= 215
                        aparicion_level3 = False
                    enemy2.moves_x(direccion_enemy)
                    enemy2.upgrade()
                    enemy2.dibujar(screen)
                    if player1.rect.colliderect(enemy2.rect):
                        game_over_flag = True
                    if flag_coin3 == True:
                        bandera3.upgrade()
                        bandera3.dibujar(screen)
                        if player1.rect.colliderect(bandera3.rect):
                            level1 = False
                            level2 = False
                            level3 = False
                            fin_timer = True
                            win_flag = True
                            game_over_flag = True
                player1.upgrade()
                player1.dibujar(screen, accion_personaje, direccion)
                screen.blit(text_score,(325,10))
                screen.blit(text_time,(10,10))
        if game_over_flag == True:
            screen.blit(win_img,(0,0)) # Ubicacion del fondo
            screen.blit(text_restart,(10,450))
            screen.blit(text_menu,(390,450))
            if win_flag == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if(event.key >= pygame.K_a and event.key <= pygame.K_z):
                            letra = chr(event.key).upper()
                            re.search('[a-z]+', letra)
                            usuario = list(usuario)
                            usuario.append(letra)
                            if len(usuario) == 5:
                                nuevo_usuario = []
                                usuario = "".join(usuario)
                                nuevo_usuario.append(usuario)
                                nuevo_usuario.append(str(segundos))
                                nuevo_usuario = ",".join(nuevo_usuario)
                                usuario = []
                                segundos = 0
                usuario = "".join(usuario)
                text_usuario = font.render(usuario, True, (255, 255, 255))
                rectangulo = pygame.Rect((150, 50), (200,100))
                pygame.draw.rect(screen, (155, 155, 155), rectangulo)
                screen.blit(text_usuario,(150, 50))
                screen.blit(text_save,(205,450))
    pygame.display.flip()# Muestra los cambios en la pantalla
    milis.tick(FPS)
pygame.quit() # Fin