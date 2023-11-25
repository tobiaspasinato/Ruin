import pygame
import random
from constants import *

def get_animacion(path, columnas, filas, flip = False):
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
            if flip == True:
                surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)
            lista.append(surface_fotograma)
    return lista

class enemy:
    def __init__(self, x : int, y : int) -> None:
        self.stay_r = get_animacion("imgs\enemy.png", 5, 1)
        self.stay_i = get_animacion("imgs\enemy.png", 5, 1)
        self.frame = 0
        self.move_x = x
        self.move_y = y
        self.animation = self.stay_i
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
    
    def moves(self, dirreccion):
        if dirreccion == True:
            self.move_y = -2
        if dirreccion == False:
            self.move_y = 2
    
    def upgrade(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
        
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.move_x = 0
        self.move_y = 0
    
    def dibujar(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)