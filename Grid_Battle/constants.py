import pygame

#FPS
FPS = 60

#TITLE
TITLE = 'Grid - Battle Base System'

#SIZE
WIDTH = 704
HEIGHT = 480
TILESIZE = 32

#CHESSBOARD_X = 40
#CHESSBOARD_Y = 40

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

#stat a changer
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

ENEMY_ATTRIBUTE = { 
    'x' : 289 ,
    'y' : 32 ,
    'width' : 32,
    'height' : 32 ,
    'color' : RED ,
    'atk' : 25,
    'hp' : 100,
    'name' : 'enemy'
}

POSSIBLE_MOVEMENTS = {
    "top": [1, 1, 1, 1, 1],
    "left": [1, 1, 1, 1, 1],
    "right": [1, 1, 1, 1, 1],
    "bottom": [1, 1, 1, 1, 1]
}

POSSIBLE_ATTACKS = {
    "top": [1, 1, 1, 1, 1],
    "top-left": [1, 1, 1, 1],
    "top-right": [1, 1, 1, 1],
    "left": [1, 1, 1, 1, 1],
    "right": [1, 1, 1, 1, 1],
    "bottom": [1, 1, 1, 1, 1],
    "bottom-left": [1, 1, 1,1],
    "bottom-right": [1, 1,1,1]
}

PIC_DICTIONARY = {
    "Character_Idle": [],
    "Character_Walking_Front": [],
    "Character_Attack": []
}

E_PIC_DICTIONARY = {
    "Monster": []
}