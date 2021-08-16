import pygame as pg

class Pikachu(pg.sprite.Sprite):

    def __init__(self, width, height, windowWidth, windowHeight, tela):
        self.width = width
        self.height = height
        self.img = pg.transform.scale(pg.image.load("Assets/pikachuskate.png"), (self.width, self.height))
        self.velocidadeX = 0.27
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = windowWidth/2 - width/2
        self.y = 600
        self.tela = tela
        self.direcao = -1
    
    def draw(self):
        self.tela.blit(self.img, (self.x, self.y))


    def update(self):
        comandos = pg.key.get_pressed()
        if comandos[pg.K_RIGHT] and not(self.x >= self.windowWidth-self.width):
            self.x += self.velocidadeX
            if self.direcao == -1:
                self.img = pg.transform.flip(self.img, True, False)
            self.direcao = 1
        if comandos[pg.K_LEFT] and not(self.x <= 0):
            self.x -= self.velocidadeX
            if self.direcao == 1:
                self.img = pg.transform.flip(self.img, True, False)
            self.direcao = -1
  





