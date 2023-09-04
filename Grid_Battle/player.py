import pygame
from .characters import *
from .gui import *
from .constants import *
from .state import GameState
from .dataWork import load_image

class Player(Characters):
    def __init__(self, x, y, width, height, color, atk , hp, name):
        super().__init__(x, y, width, height, color, atk , hp, name)
        self.__state = GameState()
        self.index = 0
        #on défini un liste de vide pour contenir les images d'animations du joueur (lorsqu'il attaque, qu'il marche ou qu'il reste immobile)
        self.idle = []
        self.walk_front = []
        self.attacking = []
        self.load_images()
        # self.image = self.attacking[0]
        #elapsed sert pour check les temps entre les animations
        self.elapsed = 0
    
    def load_images(self):#permet de charger les images liées au joueur (spritesheet)
        for dirr, values in PIC_DICTIONARY.items():
            for value in values:
                if dirr == "Character_Idle":
                    self.idle.append(load_image(self, dirr, value)) #load_image est la fonction présente dans dataWork
                elif dirr == "Character_Walking_Front":
                    self.walk_front.append(load_image(self, dirr, value))
                elif dirr == "Character_Attack":
                    self.attacking.append(load_image(self, dirr, value))
    
    def animation(self): #fonction pour animé le joueur lorsqu'il reste sur place, qu'il bouge, ou qu'il attaque
        now = pygame.time.get_ticks()
        if self.get_state() == "idle":
            if now - self.elapsed > 250:
                self.elapsed = now
                self.index += 1
                if self.index >= len(self.idle):
                    self.index = 0
                self.image = self.idle[self.index]
        elif self.get_state() == "moving":
            if now - self.elapsed > 250:
                self.elapsed = now
                self.index += 1
                if self.index >= len(self.walk_front):
                    self.index = 0
                self.image = self.walk_front[self.index]
        if self.get_state() == "attacking":
            if now - self.elapsed > 250:
                self.elapsed = now
                self.index += 1
                try:
                    if self.index >= len(self.attacking):
                        self.index = 0
                    self.image = self.attacking[self.index]
                except IndexError:
                    self.index = 0
        self.image.set_colorkey(BLACK)#permet d'enlever le background noir des sprites
    
    def update(self): # permet de mettre à jour l'animation du joueur
        self.animation()

    def player_controller(self): #création des controller pour le joueur (bouton pour faire des actions dans le jeu)
        #on défini un Gui pour chaque action du joueur
        self.attack_button = Gui()
        self.walk_button = Gui()
        self.change_button = Gui()

        # on défini l'emplacement des boutons pour chaque action du joueur
        self.walk_button.new_button(WIDTH - 145, HEIGHT - 80, 64, 64, "Walk")
        self.change_button.new_button(WIDTH - 230, HEIGHT - 80,80, 64, "Change")
        self.attack_button.new_button(WIDTH - 80, HEIGHT - 80, 75, 64, "Attack")

    def actions(self, event):#fonction permettant de faire bouger le personnage après avoir activé l'état "moving"
        self.mouse_rect_init = pygame.Surface((self.width, self.height))
        self.mouse_rect = self.mouse_rect_init.get_rect()
        self.mouse_rect.x, self.mouse_rect.y = pygame.mouse.get_pos()
        for squa in self.squares:
            if event.type == pygame.MOUSEBUTTONDOWN and squa.rect.collidepoint(self.mouse_rect.x, self.mouse_rect.y) and self.get_state() == "moving":
                self.rect.x = squa.rect.x
                self.rect.y = squa.rect.y
                self.squares.clear()
                self.set_idle()

    
    def update_controller(self, frame): #mis a jour de chaque bouton du joueur
        self.attack_button.update(frame)
        self.walk_button.update(frame)
        self.change_button.update(frame)
        #on vérifie si un des boutons a été cliqué par le joueur
        self.switch()
    
    def controller_event_handler(self, event): #gere les evenement correspondant a chaque action du joueur
        self.attack_button.event(event)
        self.walk_button.event(event)
        self.change_button.event(event)

    def controller_screen_draw(self, screen): # dessin des boutons dans le jeu
        self.attack_button.draw(screen)
        self.walk_button.draw(screen)
        self.change_button.draw(screen)

    def action_posibility(self, screen):
        if self.get_state() == "attacking":
            self.show_posibilities_attack(screen)

        elif self.get_state() == "moving":
            self.show_posibilities_move(screen)

    def basic_attack(self, target, event): #si l'attack touche la case d'un enemy on diminue les pv de l'ennemi
        if self.get_state() == "attacking" and target:
            if event.type == pygame.MOUSEBUTTONDOWN and target.rect.collidepoint(pygame.mouse.get_pos()):
                raw_damage = target.hp - self.atk 
                target.hp = raw_damage
                print(target.hp)
                self.set_idle()

    def switch(self): #cette fonction permet de changé d'état de jeu en fonction des bouton appuyer par le joueur
        for button in [self.attack_button, self.change_button, self.walk_button]:
            if button.what_pressed() == self.attack_button:
                self.set_fight()
            elif button.what_pressed() == self.walk_button:
                self.set_move()
            elif button.what_pressed() == self.change_button:
                self.set_idle()

    def set_idle(self):
        #squares est un tableau présent dans Characters. cela affiche les zones d'attaque ou de mouvement du joueur
        #ici on efface l'affichage de ce zones pour remettre la grid dans ces couleurs initiales
        self.squares.clear()
        #on change l'état actuelle pour mettre l'état idle avec le trigger "stop"
        return self.__state.stop()

    def set_fight(self):
        #on change l'état actuelle pour mettre l'état attacking avec le trigger "fight"
        return self.__state.fight()

    def set_move(self):
        #on change l'état actuelle pour mettre l'état walking avec le trigger "walk"
        return self.__state.walk()

    def get_state(self):
        return str(self.__state)
