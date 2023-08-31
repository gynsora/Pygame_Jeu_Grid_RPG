import pygame
from .characters import *

class Enemy(Characters):
    def __init__(self, x, y, width, height, color, atk , hp, name):
        super().__init__(x, y, width, height, color, atk , hp, name)
        self.index = 0
        self.idle = [] 
        # self.load_images()
        self.elapsed = 0