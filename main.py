from inimigos import *
from movimentos import *
import pygame as pg
pg.init()

largura, altura = 600, 720


tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('Jorginho')

inimigos = pg.sprite.Group()
pikachu = Pikachu(120,120, largura, altura, tela)
inimigos.add(Farfetch(80, 80, largura, altura, tela))
inimigos.add(Pidgeot(100, 100, largura, altura, tela))
inimigos.add(Zubat(60, 60, largura, altura, tela))
inimigos.add(Dragonite(160, 160, largura, altura, tela))

background = pg.image.load("Assets/background.jpeg")

while True:
  tela.fill((0,0,0))
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()
  tela.blit(background,(0,0))
  pikachu.draw()
  pikachu.update()
  inimigos.draw(tela)
  inimigos.update()


  pg.display.update()