import pygame as pg
from inimigos import *
from movimentos import *
from vida import *


pg.init()

clock = pg.time.Clock()
font = pg.font.Font(None,30)

largura, altura = 600, 720


tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('Jorginho')

inimigos = pg.sprite.Group()
pikachu = Pikachu(110,110, largura, altura, tela)

inimigos.add(Farfetch(80, 80, largura, altura, tela))
inimigos.add(Pidgeot(100, 100, largura, altura, tela))
inimigos.add(Zubat(60, 60, largura, altura, tela))
inimigos.add(Dragonite(160, 160, largura, altura, tela))

berries = pg.sprite.Group()
bala = pg.sprite.Group()


background = pg.image.load("Assets/background.jpeg")

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()
  
  tela.blit(background,(0,0))
  
  pikachu.draw()
  pikachu.update()

  inimigos.draw(tela)
  inimigos.update(bala, berries)

  berries.draw(tela)
  berries.update()

  bala.draw(tela)
  bala.update()

  fps = font.render(str(int(clock.get_fps())),True,"WHITE")
  tela.blit(fps,(50,50))
  clock.tick(60)

  if General.check_collision(pikachu, berries):
    Player.player_gain(pikachu)

  if General.check_collision(pikachu, inimigos):
    Player.player_loss(pikachu)
        #tem que acabar com o jogo aqui

  pg.display.update()