import pygame as pg
from random import randint
import random
from acoes import *
from extras import *


class Farfetch(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela, sound):
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
    self.x = randint(0, self.windowWidth-self.width-1)
    self.y = -height
    self.tela = tela
    self.rect = self.image.get_rect()
    self.life = 1
    self.sound = sound
    
  #Atualiza o Farfetch na tela
  def update(self, bullet, berries, pikachu, item, sound):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      sound.play()
      if General.is_dead(self):
        soma_pontos(25)
        #gerar berry
        parameter = random.randint(0, 10)
        if parameter == 1:
          parameter2 = random.randint(0, 1)
          if parameter2 == 1:
            item.add(Buff(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))
          else:
            berries.add(Berry(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))
    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    self.x += self.velocidadeX
    if self.y >= self.windowHeight - self.height :
      self.sound.play
      self.kill()
      if Player.player_loss(pikachu):
        pg.quit()
    if self.x >= self.windowWidth-self.width:
      self.image = pg.transform.flip(self.image, True, False)
      self.velocidadeX = -self.velocidadeX
    if self.x <= -20:
      self.image = pg.transform.flip(self.image, True, False)
      self.velocidadeX = -self.velocidadeX
    self.rect.topleft = (self.x, self.y)
    

class Zubat(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo zubat
  def __init__(self, width, height, windowWidth, windowHeight, tela,sound):
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
    self.sound = sound

  #Atualiza o zubat na tela
  def update(self, bullet, berries, pikachu, item, sound):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      sound.play()
      if General.is_dead(self):
        soma_pontos(10)
        #gerar berry
        parameter = random.randint(0, 10)
        if parameter == 1:
          parameter2 = random.randint(0, 2)
          if parameter2 == 1:
            item.add(Buff(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))
          else:
            berries.add(Berry(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))
          
    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    if self.y >= self.windowHeight - self.height :
      self.sound.play()
      self.kill()
      if Player.player_loss(pikachu):
        pg.quit()
    self.rect.topleft = (self.x,self.y)

class Dragonite(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo dragonite
  def __init__(self, width, height, windowWidth, windowHeight, tela, sound):
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
    self.sound = sound
    

  def update(self, bullet, berries, pikachu, item, sound):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      sound.play()
      if General.is_dead(self):
        soma_pontos(100)
        #gerar berry
        parameter = random.randint(0, 10)
        if parameter == 1:
          parameter2 = random.randint(0, 2)
          if parameter2 == 1:
            item.add(Buff(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))
          else:
            berries.add(Berry(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))

    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    if self.y >= self.windowHeight - self.height :
      self.sound.play()
      self.kill()
      if Player.player_loss(pikachu):
        pg.quit()
    self.rect.topleft = (self.x,self.y)

class Pidgeot(pg.sprite.Sprite):
  # Classe responsável por criar o inimigo Pidgeot
  def __init__(self, width, height, windowWidth, windowHeight, tela, sound):
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
    self.sound = sound

  #atualiza o pidgeot na tela
  def update(self, bullet, berries, pikachu, item, sound):

    if General.check_collision(self, bullet):
      Enemy.enemy_loss(self)
      sound.play()
      if General.is_dead(self):
        soma_pontos(50)
        #gerar berry
        parameter = random.randint(0, 10)
        if parameter == 1:
          parameter2 = random.randint(0, 2)
          if parameter2 == 1:
            item.add(Buff(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))
          else:
            berries.add(Berry(self.windowWidth,self.windowHeight, self.tela, self.x + self.width/2 - 15, self.y + self.height/2 - 15))
          
    # movimenta o pokemon de acordo com a velocidade.
    self.y += self.velocidadeY
    if self.y >= self.windowHeight - self.height :
      self.sound.play()
      self.kill()
      if Player.player_loss(pikachu):
        pg.quit()
    self.rect.topleft = (self.x,self.y)


# Classe responsável por criar o pikachu
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
      self.intervalo = 500
      self.tempo = 10

  #Cria o desenho do pikachu
  def draw(self):
      self.tela.blit(self.image, (self.x, self.y))

  #atualiza o pikachu na tela
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
          if tempo - self.tempoAnterior >= self.intervalo:
              bala.add(Bullet(self.x+self.width/2, self.y, self.tela))
              self.tempoAnterior = pg.time.get_ticks()
      self.rect.topleft = (self.x, self.y)

#Gambiarra que faz a pontuação
ponto = 0
def soma_pontos(pontos):
  global ponto
  ponto += pontos
  return ponto
