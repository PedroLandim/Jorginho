import pygame as pg
from random import randint

class Farfetch(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela):
    angulo = 25
    self.width = width
    self.height = height
    self.img = pg.transform.scale(pg.image.load('assets/farfetch.png'), (self.width, self.height))
    self.img = pg.transform.rotate(self.img, angulo)
    self.img = pg.transform.flip(self.img, True, False)
    self.velocidadeY = 0.15
    self.velocidadeX = 0.18
    self.windowWidth = windowWidth
    self.windowHeight = windowHeight
    self.x = randint(0, self.windowWidth-self.width)
    self.y = -height
    self.tela = tela
    
  def draw(self):
    #desenha a imagem na tela do jogo.
    self.tela.blit(self.img, (self.x,self.y))

  def update(self):
    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    self.x += self.velocidadeX
    if self.y >= self.windowHeight:
      self.y = -self.height
      self.x = randint(0, self.windowWidth-self.width)
    if self.x >= self.windowWidth-self.width*4/5:
      self.img = pg.transform.flip(self.img, True, False)
      self.velocidadeX = -self.velocidadeX
    if self.x <= -self.width/5:
      self.img = pg.transform.flip(self.img, True, False)
      self.velocidadeX = -self.velocidadeX