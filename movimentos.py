import pygame as pg

class Pikachu(pg.sprite.Sprite):

    def __init__(self, width, height, windowWidth, windowHeight, tela):
        self.width = width
        self.height = height
        self.img = pg.transform.scale(pg.image.load("Assets/pikachuskate.png"), (self.width, self.height))
        self.velocidadeX = 0.17
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = windowWidth/2 - width/2
        self.y = 600
        self.tela = tela
    
    def draw(self):
        self.tela.blit(self.img, (self.x, self.y))

    def move(self):
        comandos = pg.key.get_pressed()
        if comandos[pg.K_RIGHT]:
            self.x += self.velocidadeX
            self.img = pg.transform.flip(self.img, True, False)
        if comandos[pg.K_LEFT]:
            self.x += -self.velocidadeX
            self.img = pg.transform.flip(self.img, True, False)

