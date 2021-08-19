import pygame as pg
from bullets import Bullet

class Pikachu(pg.sprite.Sprite):

    def __init__(self, width, height, windowWidth, windowHeight, tela):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pg.transform.scale(pg.image.load("Assets/pikachuskatista.png"), (self.width, self.height))
        self.velocidadeX = 3
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = windowWidth/2 - width/2
        self.y = 610
        self.tela = tela
        self.direcao = -1
        self.life = 3
        self.rect = self.image.get_rect()
        self.tempoAnterior = 0

    
    def draw(self):
        self.tela.blit(self.image, (self.x, self.y))


    def update(self, bala, tempo):
        comandos = pg.key.get_pressed()
        if comandos[pg.K_RIGHT] and self.x < self.windowWidth-self.width:
            self.x += self.velocidadeX
            if self.direcao == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.direcao = 1
        if comandos[pg.K_LEFT] and self.x > 0:
            self.x -= self.velocidadeX
            if self.direcao == 1:
                self.image = pg.transform.flip(self.image, True, False)
            self.direcao = -1
        if comandos[pg.K_SPACE]:
            if tempo - self.tempoAnterior >= 500:
                bala.add(Bullet(self.x+self.width/2, self.y, self.tela))
                self.tempoAnterior = pg.time.get_ticks()
        self.rect.topleft = (self.x, self.y)





