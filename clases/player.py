import pygame

def get_animacion(path, columna, filas):
    lista = []
    surface_imagen = pygame.image.load(path)
    lista.append(surface_imagen)
    return lista

class player:
    def __init__(self) -> None:
        self.walk = get_animacion("imgs\player_run.png", 4, 1)
        self.stay = []
        self.frame = 0
        self.animation = self.walk
        self.image = self.animation[self.frame]
        self.react = self.image.get_react()
        pass
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.react)
