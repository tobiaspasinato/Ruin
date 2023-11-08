import pygame

def get_animacion():
    lista = []
    return lista

class player:
    def __init__(self) -> None:
        self.walk = []
        self.stay = []
        self.frame = 0
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.react = self.image.get_react()
        pass