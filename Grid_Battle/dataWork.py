import pygame
import os
from .constants import PIC_DICTIONARY, E_PIC_DICTIONARY


directory = os.path.join(os.path.dirname(__file__), "assets\img")

def load_image(target, dirr, name):
    # print(os.path.join(directory, dirr + "\\" + name))
    sprite = pygame.image.load(os.path.join(directory, dirr + "/" + name)).convert()
    image = pygame.Surface((target.width, target.height))
    image.blit(sprite, (1, 1))
    return image

def filled_up(dirr, var):
    # print(os.listdir(directory+"/Character_Attack"))
    character_quantity = [name for name in os.listdir(directory+"\\"+dirr)]
    for name in character_quantity:
        var.append(name)

def filled(dicts):
    for k, v in dicts.items():
        filled_up(k, v)

filled(PIC_DICTIONARY)
filled(E_PIC_DICTIONARY)