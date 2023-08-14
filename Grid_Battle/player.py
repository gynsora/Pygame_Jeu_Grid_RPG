import pygame
from .characters import *
from .gui import *
from .constants import *

class Player(Characters):
    def __init__(self, x, y, width, height, color, atk , hp, name):
        super().__init__(x, y, width, height, color, atk , hp, name)

    def player_controller(self): #création des controller pour le joueur (bouton pour faire des actions dans le jeu)
        #on défini un Gui pour chaque action du joueur
        self.attack_button = Gui()
        self.walk_button = Gui()
        self.change_button = Gui()

        # on défini l'emplacement des boutons pour chaque action du joueur
        self.walk_button.new_button(WIDTH - 145, HEIGHT - 80, 64, 64, "Walk")
        self.change_button.new_button(WIDTH - 230, HEIGHT - 80,80, 64, "Change")
        self.attack_button.new_button(WIDTH - 80, HEIGHT - 80, 75, 64, "Attack")
    
    def update_controller(self, frame): #mis a jour de chaque bouton du joueur
        self.attack_button.update(frame)
        self.walk_button.update(frame)
        self.change_button.update(frame)
        #self.switch()
    
    def controller_event_handler(self, event): #gere les evenement correspondant a chaque action du joueur
        self.attack_button.event(event)
        self.walk_button.event(event)
        self.change_button.event(event)

    def controller_screen_draw(self, screen): # dessin des boutons dans le jeu
        self.attack_button.draw(screen)
        self.walk_button.draw(screen)
        self.change_button.draw(screen)

    def action_posibility(self, screen):
        #self.show_posibilities_move(screen)
        self.show_posibilities_attack(screen)
        
        # if self.get_state() == "attacking":
        #     self.show_posibilities_attack(screen)

        # elif self.get_state() == "moving":
        #     self.show_posibilities_move(screen)
