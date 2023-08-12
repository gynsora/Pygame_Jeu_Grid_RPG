import pygame

#FPS
FPS = 60

#TITLE
TITLE = 'Grid - Battle Base System'

#SIZE
WIDTH = 704
HEIGHT = 480
TILESIZE = 32

#FONT
FONTNAME = 'comicsans'
FONTSIZE = 24

# COLOR
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
LIGHTBLUE  = (0,155,155)
LIGHTYELLOW = (255,255,102)


PLAYER_ATTRIBUTE = { 
    'x' : 289 ,
    'y' : 193 ,
    'width' : 32,
    'height' : 32 ,
    'color' : GREEN ,
    'atk' : 25,
    'hp' : 100,
    'name' : 'gynz'
}