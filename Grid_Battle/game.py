import pygame
from .constants import *
from .player import Player
class Game:
    def __init__(self, win):#initialisation du jeu
        self.win = win
        self.run = True
        pygame.init() #initialisation de pygame TRES IMPORTANT
        pygame.font.init()
        self.generic_font = pygame.font.SysFont(FONTNAME,FONTSIZE)
        self.new()

    def new(self):#création du joueur et de ses sort
        self.all_sprites = pygame.sprite.Group() 
        self.player = Player(*PLAYER_ATTRIBUTE.values())#on passe en parametre tout les attributs du joueur (attention à l'ordre des attributs)
        self.all_sprites.add(self.player)
        self.player.player_controller()
    
    def event(self):#eventListener du jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
                self.run = False
            self.player.controller_event_handler(event)

    def update(self): #update du jeu
        self.player.update_controller(FPS)
        self.draw()
        pygame.display.update()

    def draw_grid(self): #dessin de la grid de jeu
        #Vertical lines
        #for x in range(CHESSBOARD_X, CHESSBOARD_X+TILESIZE*6 , TILESIZE):
            #pygame.draw.line(self.win, YELLOW , (x,CHESSBOARD_Y),(x,CHESSBOARD_Y+TILESIZE*5 ))
        #Horizontal lines
        #for y in range(CHESSBOARD_Y, CHESSBOARD_Y+TILESIZE*6 ,TILESIZE):
            #pygame.draw.line(self.win, YELLOW , (CHESSBOARD_X,y),(CHESSBOARD_X+TILESIZE*5,y))

        #Vertical lines
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.win, LIGHTBLUE , (x,0),(x,HEIGHT))
        #Horizontal lines
        for y in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.win, LIGHTBLUE , (0,y),(WIDTH,y))
        
    def draw(self):
        self.win.fill(BLACK)
        self.all_sprites.draw(self.win)
        self.player.action_posibility(self.win)
        self.draw_grid()
        self.player.controller_screen_draw(self.win)
        #hits_label =  self.generic_font.render(f"Hits: ", 1, "white")
        #self.win.blit(hits_label, (450, 5))
        pygame.display.flip()

     