import pygame

class Characters(pygame.sprite.Sprite):
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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        