import pygame
from constants import *

def get_animacion(path, columnas, filas, direccion = True):
    lista = []
    surface_imagen = pygame.image.load(path)
    fotograma_ancho = int(surface_imagen.get_width()/columnas)
    fotograma_alto = int(surface_imagen.get_height()/filas)
    x = 0
    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
            lista.append(surface_fotograma)
    return lista

def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
    for img in lista_original:
        lista_girada.append(pygame.transform.flip(img, flip_x, flip_y))
    return lista_girada

class player:
    def __init__(self) -> None:
        self.walk = get_animacion("imgs\player_run.png", 4, 1)
        self.stay = get_animacion("imgs\player_stay.png", 4, 1)
        self.hit = get_animacion("imgs\player_atack_3.png", 5, 1)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.walk_i = girar_imagenes(self.walk, True, False)
        self.stay_i = girar_imagenes(self.stay, True, False)
        self.hit_i = girar_imagenes(self.hit, True, False)
    
    def control(self, x, y):
        self.move_x = x
        self.move_y = y
    
    def upgrade(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
        
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.move_x = 0
        self.move_y = 0

    
    def dibujar(self, screen, accion, direccion):
        if direccion == True:
            if accion == "stay":
                self.animation = self.stay
                self.image = self.animation[self.frame]
            elif accion == "walk":
                self.animation = self.walk
                self.image = self.animation[self.frame]
            elif accion == "atack":
                self.animation = self.hit
                self.image = self.animation[self.frame]
        else:
            if accion == "atack":
                self.animation = self.stay_i
                self.image = self.animation[self.frame]
            elif accion == "atack":
                self.animation = self.walk_i
                self.image = self.animation[self.frame]
            elif accion == "atack":
                self.animation = self.hit_i
                self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
