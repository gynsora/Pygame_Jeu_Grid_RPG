import pygame
from .characters import *
from .dataWork import load_image

class Enemy(Characters):
    def __init__(self, x, y, width, height, color, atk , hp, name):
        super().__init__(x, y, width, height, color, atk , hp, name)
        self.index = 0
        self.idle = [] 
        self.load_images()
        self.elapsed = 0

    def load_images(self):
        for dirr, values in E_PIC_DICTIONARY.items():
            for value in values:
                if dirr == "Monster":
                    self.idle.append(load_image(self, dirr, value))

    def animation(self):
        now = pygame.time.get_ticks()
        if now - self.elapsed > 250:
            self.elapsed = now 
            self.index += 1
            try:
                if self.index >= len(self.idle):
                    self.index = 0
                self.image = self.idle[self.index]
            except IndexError:
                self.index = 0
        self.image.set_colorkey(BLACK)

    def update(self):
        self.animation()