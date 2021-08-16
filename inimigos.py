import pygame
from sys import exit
from random import randint


pygame.init()

class Farfetch(pygame.sprite.Sprite):
  # Classe responsável por criar o inimigo farfetch
  def __init__(self, width, height, windowWidth, windowHeight, tela):
    angulo = 25
    self.width = width
    self.height = height
    self.img = pygame.transform.scale(pygame.image.load('assets/farfetch.png'), (self.width, self.height))
    self.img = pygame.transform.rotate(self.img, angulo)
    self.img = pygame.transform.flip(self.img, True, False)
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
      self.img = pygame.transform.flip(self.img, True, False)
      self.velocidadeX = -self.velocidadeX
    if self.x <= -self.width/5:
      self.img = pygame.transform.flip(self.img, True, False)
      self.velocidadeX = -self.velocidadeX


largura, altura = 600, 720


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jorginho')


farfetch = Farfetch(80, 80, largura, altura, tela)
background = pygame.image.load("Assets/background.jpeg")
while True:
  tela.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  tela.blit(background,(0,0))
  farfetch.draw()
  farfetch.update(farfetch.x, farfetch.y)

  pygame.display.update()