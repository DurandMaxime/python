import pygame
from player import Player

# Creer une seconde class qui va representer notre jeu
class Game:

    def __init__(self):
        # generer notre joueur
        self.player = Player()
        self.pressed = {}