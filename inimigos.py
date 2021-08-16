import pygame as pg
from sys import exit
from random import randint


pg.init()

class Farfetch(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela):
    angulo = 25
    self.width = width
    self.height = height
    self.img = pg.transform.scale(pg.image.load('assets/farfetch.png'), (self.width, self.height))
    self.img = pg.transform.rotate(self.img, angulo)
    self.img = pg.transform.flip(self.img, True, False)
    self.velocidadeY = 0.32
    self.velocidadeX = 0.29
    self.windowWidth = windowWidth
    self.windowHeight = windowHeight
    self.x = randint(0, self.windowWidth-self.width)
    self.y = -height
    self.tela = tela
    
  def draw(self):
    #desenha a imagem na tela do jogo.
    self.tela.blit(self.img, (self.x,self.y))

  def update(self, x, y):
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


largura, altura = 600, 720


tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('Jorginho')


farfetch = Farfetch(80, 80, largura, altura, tela)
background = pg.image.load("Assets/background.jpeg")
while True:
  tela.fill((0,0,0))
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()
  tela.blit(background,(0,0))
  farfetch.draw()
  farfetch.update(farfetch.x, farfetch.y)

  pg.display.update()