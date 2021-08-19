import pygame as pg
from inimigos import *
from movimentos import *
from vida import *

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, tela):

        super().__init__()

        self.image = pg.image.load('assets/relampago.png') 
        self.rect = self.image.get_rect()
        self.tela = tela
        self.x = x
        self.y = y

        #posicao inicial
        self.rect = self.image.get_rect()

        #velocidade
        self.speed = 5


    def update(self):
        self.y -= self.speed
        if self.y <= 0:
            self.kill()
        #aqui tem que criar if bater no pokemon ela se destroi, senao passa direto ate o final da tela
        self.rect.center = (self.x, self.y)