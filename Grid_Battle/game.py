import pygame
from .constants import *
from .player import Player
class Game:
    def __init__(self, win):
        self.win = win
        self.run = True
        pygame.init() #initialisation de pygame TRES IMPORTANT
        pygame.font.init()
        self.generic_font = pygame.font.SysFont(FONTNAME,FONTSIZE)
        self.new()

    def new(self):
        self.all_sprites = pygame.sprite.Group() 
        self.player = Player(*PLAYER_ATTRIBUTE.values())#on passe en parametre tout les attributs du joueur (attention à l'ordre des attributs)
        self.all_sprites.add(self.player)
        self.player.player_controller()
    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
                self.run = False
            self.player.controller_event_handler(event)

    def update(self):
        self.player.update_controller(FPS)
        self.draw()
        pygame.display.update()

    def draw(self):
        self.win.fill(BLACK)
        self.all_sprites.draw(self.win)
        self.player.controller_screen_draw(self.win)
        #hits_label =  self.generic_font.render(f"Hits: ", 1, "white")
        #self.win.blit(hits_label, (450, 5))
        pygame.display.flip()

     