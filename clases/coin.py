import pygame
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
            surface_fotograma = pygame.transform.scale(surface_fotograma, (25, 25))
            lista.append(surface_fotograma)
    return lista

class coin:
    def __init__(self, x : int, y : int) -> None:
        self.stay = get_animacion("Ruin/imgs/coin.png", 6, 1)
        self.frame = 0
        self.move_x = x
        self.move_y = y
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
    
    def imprimir_rect(self):
        print(self.rect)
    
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
        self.animation = self.stay
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)