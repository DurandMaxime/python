import pygame


class PaddleOpponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('MesProgrammes/PongGame/ressources/PongPaddlesBlue.png')
        self.rect = self.image.get_rect()                                       # rect permet de mettre l'image dans un carré et de la déplacer il faut la mettre
        self.rect.x = 1015                                           # modifie le point de spawn du sprite(joueur sur l'axe x ) 
        self.rect.y = 300


    def move_up(self):
        if self.rect.y >= 10:
            self.rect.y -= self.speed
    def move_down(self):
        if self.rect.y < (720-148):
            self.rect.y += self.speed