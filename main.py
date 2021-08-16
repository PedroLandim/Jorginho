from inimigos import *
from movimentos import *
import pygame as pg
pg.init()

largura, altura = 600, 720


tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('Jorginho')

pikachu = Pikachu(120,120, largura, altura, tela)
farfetch = Farfetch(80, 80, largura, altura, tela)
pidgeot = Pidgeot(100, 100, largura, altura, tela)
zubat = Zubat(60, 60, largura, altura, tela)
dragonite = Dragonite(160, 160, largura, altura, tela)
background = pg.image.load("Assets/background.jpeg")

while True:
  tela.fill((0,0,0))
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()
  tela.blit(background,(0,0))
  farfetch.draw()
  pikachu.draw()
  dragonite.draw()
  zubat.draw()
  pidgeot.draw()
  pikachu.update()
  farfetch.update()
  zubat.update()
  dragonite.update()
  pidgeot.update()

  pg.display.update()