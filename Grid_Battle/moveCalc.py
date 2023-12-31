import pygame
from .constants import *

class MoveCalc(pygame.sprite.Sprite):
    def __init__(self,x,y): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        #ajouter un argument pour recupérer le type de sort choisi (deplacement, sort)
        #modifier image.fill pour avoir des tile transparente 
        self.image.fill(LIGHTYELLOW)
        self.image.set_alpha(128) #opacity
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def calc_movement(self,target): # faire cette fonction avec une matrice a 2 dimension pour utilisé les coordonées plus facilement
        coordinates = []
        for k, v in POSSIBLE_MOVEMENTS.items():
            if k == "top":
                for _ in range(0, len(v)):
                    self.rect.x = target.rect.x
                    self.rect.y -= TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))
            
            elif k == "left":
                for _ in range(0, len(v)):
                    self.rect.x -= TILESIZE
                    self.rect.y = target.rect.y
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "right":
                self.rect.x = target.rect.x
                for _ in range(0, len(v)):
                    self.rect.x += TILESIZE
                    self.rect.y = target.rect.y
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom":
                for _ in range(0, len(v)):
                    self.rect.x = target.rect.x
                    self.rect.y += TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))
        
        return coordinates
    
    def cal_attack_options(self, target):
        coordinates = []

        for k, v in POSSIBLE_ATTACKS.items():

            if k == "top":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y

                for _ in range(0, len(v)):
                    self.rect.y -= TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "top-right":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):

                    self.rect.x += TILESIZE
                    self.rect.y -= TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "top-left":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.x -= TILESIZE
                    self.rect.y -= TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "right":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.x -= TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "left":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.x += TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom-right":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.y += TILESIZE
                    self.rect.x += TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom-left":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.y += TILESIZE
                    self.rect.x -= TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.y += TILESIZE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

        return coordinates