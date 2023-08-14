import pygame
from .constants import *
from .moveCalc import MoveCalc

class Characters(pygame.sprite.Sprite):#stat su joueur
    def __init__(self, x, y, width, height, color, atk , hp, name):
        pygame.sprite.Sprite.__init__(self)
        self.atk = atk
        self.hp = hp
        self.width = width
        self.height = height
        self.name = name
        self.color = color
        self.image = pygame.Surface((width,height))
        self.image.fill(self.color)
        #self.image = pygame.Surface((width,height), pygame.SRCALPHA)
        #self.image.fill((255,255,255,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.squares = []

        #faire des rectangles semi transparent pour la portée des sorts
        #s = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha
        #s.fill((255,255,255,128))                         # notice the alpha value in the color
        #windowSurface.blit(s, (0,0))

    def show_posibilities_move(self, g):
        self.calculation = MoveCalc(self.rect.x, self.rect.y)#on calcule la portée de mouvement du joueur
        for top, left in self.calculation.calc_movement(self):#ici la portée de mouvement se calcule avec une cible, cette cible (target) est le joueur lui même
            self.square = MoveCalc(top, left)
            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.square)
            self.all_sprites.draw(g)
            self.squares.append(self.square)
    
    def show_posibilities_attack(self, g):
        self.calculation = MoveCalc(self.rect.x, self.rect.y)#on calcule la portée d'attack du joueur
        for top, left in self.calculation.cal_attack_options(self):#ici la portée de mouvement se calcule avec une cible, cette cible (target) est le joueur lui même
            self.square = MoveCalc(top, left)
            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.square)
            self.all_sprites.draw(g)
            self.squares.append(self.square)
    