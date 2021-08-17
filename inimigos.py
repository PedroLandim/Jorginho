import pygame as pg
from random import randint
import random
from vida import *


class Farfetch(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela):
    super().__init__()
    angulo = 25
    self.width = width
    self.height = height
    self.image = pg.transform.scale(pg.image.load('assets/farfetch.png'), (self.width, self.height))
    self.image = pg.transform.rotate(self.image, angulo)
    self.image = pg.transform.flip(self.image, True, False)
    self.velocidadeY = 1.5
    self.velocidadeX = 1.8
    self.windowWidth = windowWidth
    self.windowHeight = windowHeight
    self.x = randint(0, self.windowWidth-self.width)
    self.y = -height
    self.tela = tela
    self.rect = self.image.get_rect()
    self.life = 1
    
  def draw(self):
    #desenha a imagem na tela do jogo.
    self.tela.blit(self.image, (self.x,self.y))

  def update(self, bullet, berries):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      if General.is_dead():
        #gerar berry
        parameter = random.randrange(0, 1)
        if parameter == 1:
          berries.add(Berry(60,60, 600, 720, self.tela, self.x, self.y))
          

    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    self.x += self.velocidadeX
    if self.y >= self.windowHeight:
      self.y = -self.height
      self.x = randint(0, self.windowWidth-self.width)
    if self.x >= self.windowWidth-self.width:
      self.image = pg.transform.flip(self.image, True, False)
      self.velocidadeX = -self.velocidadeX
    if self.x <= -20:
      self.image = pg.transform.flip(self.image, True, False)
      self.velocidadeX = -self.velocidadeX
    self.rect.topleft = (self.x, self.y)

class Zubat(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela):
    super().__init__()
    self.width = width
    self.height = height
    self.image = pg.transform.scale(pg.image.load('assets/zubat.png'), (self.width, self.height))
    self.velocidadeY = 2
    self.windowWidth = windowWidth
    self.windowHeight = windowHeight
    self.x = randint(0, self.windowWidth-self.width)
    self.y = -height
    self.tela = tela
    self.rect = self.image.get_rect()
    self.life = 1
    
  def draw(self):
    #desenha a imagem na tela do jogo.
    self.tela.blit(self.image, (self.x,self.y))

  def update(self, bullet, berries):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      if General.is_dead():
        #gerar berry
        parameter = random.randrange(0, 1)
        if parameter == 1:
          berries.add(Berry(60,60, 600, 720, self.tela, self.x, self.y))
          
    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    if self.y >= self.windowHeight:
      self.y = -self.height
      self.x = randint(0, self.windowWidth-self.width)
    self.rect.topleft = (self.x,self.y)

class Dragonite(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela):
    super().__init__()
    self.width = width
    self.height = height
    self.image = pg.transform.scale(pg.image.load('assets/dragonite.png'), (self.width, self.height))
    self.velocidadeY = 1
    self.windowWidth = windowWidth
    self.windowHeight = windowHeight
    self.x = randint(0, self.windowWidth-self.width)
    self.y = -height
    self.tela = tela
    self.rect = self.image.get_rect()
    self.life = 3
    
  def draw(self):
    #desenha a imagem na tela do jogo.
    self.tela.blit(self.image, (self.x,self.y))

  def update(self, bullet, berries):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      if General.is_dead():
        #gerar berry
        parameter = random.randrange(0, 1)
        if parameter == 1:
          berries.add(Berry(60,60, 600, 720, self.tela, self.x, self.y))

    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    if self.y >= self.windowHeight:
      self.y = -self.height
      self.x = randint(0, self.windowWidth-self.width)
    self.rect.topleft = (self.x,self.y)

class Pidgeot(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela):
    super().__init__()
    self.width = width
    self.height = height
    self.image = pg.transform.scale(pg.image.load('assets/pidgeot.png'), (self.width, self.height))
    self.velocidadeY = 3
    self.windowWidth = windowWidth
    self.windowHeight = windowHeight
    self.x = randint(0, self.windowWidth-self.width)
    self.y = -height
    self.tela = tela
    self.rect = self.image.get_rect()
    self.life = 1

  def draw(self):
    #desenha a imagem na tela do jogo.
    self.tela.blit(self.image, (self.x,self.y))

  def update(self, bullet, berries):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      if General.is_dead():
        #gerar berry
        parameter = random.randrange(0, 1)
        if parameter == 1:
          berries.add(Berry(60,60, 600, 720, self.tela, self.x, self.y))
          
    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    if self.y >= self.windowHeight:
      self.y = -self.height
      self.x = randint(0, self.windowWidth-self.width)
    self.rect.topleft = (self.x,self.y)
      
      