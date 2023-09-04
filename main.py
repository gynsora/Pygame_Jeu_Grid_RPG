import pygame
from Grid_Battle.constants import TITLE, WIDTH, HEIGHT, FPS
from Grid_Battle.game import Game


#WIN = window, ici on crée la taille de la fenetre du jeu
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#checkers = nom du jeu
pygame.display.set_caption(TITLE)

def main():
    #ici on crée un timer pour définir la vitesse de rafraichissement du jeu (FPS)
    clock = pygame.time.Clock()
    #on initialise le jeu
    game = Game(WIN)

    while game.run:
        clock.tick(FPS)
        #on regarde les events du jeu a chaque frame, game.event permet de quitter le jeu correctement
        game.event()   
        #on redessine le jeu à chaque frame  si besoin
        game.update()
    
    pygame.quit()

main()