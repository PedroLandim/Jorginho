import pygame as pg
from inimigos import *
from movimentos import *
from vida import *
from copy import copy

class Bullet(pg.sprite.Sprite):
    def __init__(self, position: tuple, direction: pg.Vector2, win: pg.Surface):

        super().__init__()

        self.image = pg.image.load('assets/relampago.png') 
        self.original_image = pg.image.load('assets/relampago.png') 
        self.rect = self.image.get_rect()

        #posicao inicial
        self.center = position
        self.rect.center = position

        #velocidade
        self.speed = 0.5

'''
    def update(self, dt):
        #aqui tem que criar if bater no pokemon ela se destroi, senao passa direto ate o final da tela
'''