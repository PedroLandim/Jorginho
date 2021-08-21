import pygame as pg
from personagens import *
from acoes import *

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

class Berry(pg.sprite.Sprite):
    #responsável por criar as berries
    def __init__(self, windowWidth, windowHeight, tela, pokemonX, pokemonY):
                super().__init__()
                self.width = 30
                self.height = 30
                self.image = pg.transform.scale(pg.image.load('assets/berry.png'), (self.width, self.height))
                self.velocidadeY = 2
                self.windowWidth = windowWidth
                self.windowHeight = windowHeight
                self.x = pokemonX
                self.y = pokemonY
                self.tela = tela
                self.rect = self.image.get_rect()
            
    def draw(self):
        #desenha a imagem na tela do jogo.
        self.tela.blit(self.image, (self.x,self.y))

    def update(self):
        # movimenta o pokemon de acordo com a velocidade.
        self.y += self.velocidadeY
        if self.y >= self.windowHeight - self.height:
            self.kill()
        self.rect.topleft = (self.x,self.y)


class Buff(pg.sprite.Sprite):
    #responsável por criar as berries
    def __init__(self, windowWidth, windowHeight, tela, pokemonX, pokemonY):
                super().__init__()
                self.width = 30
                self.height = 30
                self.image = pg.transform.scale(pg.image.load('assets/thunder-item.png'), (self.width, self.height))
                self.velocidadeY = 2
                self.windowWidth = windowWidth
                self.windowHeight = windowHeight
                self.x = pokemonX
                self.y = pokemonY
                self.tela = tela
                self.rect = self.image.get_rect()
            
    def draw(self):
        #desenha a imagem na tela do jogo.
        self.tela.blit(self.image, (self.x,self.y))

    def update(self):
        # movimenta o pokemon de acordo com a velocidade.
        self.y += self.velocidadeY
        if self.y >= self.windowHeight - self.height:
            self.kill()
        self.rect.topleft = (self.x,self.y)
