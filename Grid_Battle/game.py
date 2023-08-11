import pygame
from .constants import FONTNAME, FONTSIZE, BLACK

class Game:
    def __init__(self, win):
        self.win = win
        pygame.font.init()
        self.generic_font = pygame.font.SysFont(FONTNAME,FONTSIZE)

    def new(self):
        pass

    def update(self):
        self.draw()
        pygame.display.update()

    def draw(self):
        self.win.fill(BLACK)
        #hits_label =  self.generic_font.render(f"Hits: ", 1, "white")
        #self.win.blit(hits_label, (450, 5))
        pygame.display.flip()

     