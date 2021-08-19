import pygame as pg
from sys import exit
from inimigos import *
from movimentos import *
from vida import *


pg.init()

clock = pg.time.Clock()
font = pg.font.SysFont("arial",30)
pontos = 0

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
  mensagem = f"{pontos}"
  pontuacao = font.render(mensagem, False, "WHITE")
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()
  lista_depok = []
  for i in inimigos:
    if type(i) == Farfetch:
      lista_depok.append("F")
    if type(i) == Pidgeot:
      lista_depok.append("P")
    if type(i) == Zubat:
      lista_depok.append("Z")
    if type(i) == Dragonite:
      lista_depok.append("D")
  if "F" not in lista_depok:
    inimigos.add(Farfetch(80, 80, largura, altura, tela))
  if "P" not in lista_depok:
    inimigos.add(Pidgeot(100, 100, largura, altura, tela))
  if "Z" not in lista_depok:
    inimigos.add(Zubat(60, 60, largura, altura, tela))
  if "D" not in lista_depok:
    inimigos.add(Dragonite(160, 160, largura, altura, tela))
    
  tela.fill((0,0,0))
  tela.blit(background,(0,0))
  tela.blit(pontuacao, (30, 30))
  tempo = pg.time.get_ticks()
  pikachu.draw()
  pikachu.update(bala, tempo)
  
  inimigos.update(bala, berries)
  pontos = soma_pontos(0)
  inimigos.draw(tela)

  berries.update()
  berries.draw(tela)
  
  bala.update()
  bala.draw(tela)

  fps = font.render(str(int(clock.get_fps())),True,"WHITE")
 
  clock.tick(60)

  if General.check_collision(pikachu, berries):
    Player.player_gain(pikachu)

  if General.check_collision(pikachu, inimigos):
    if Player.player_loss(pikachu):
      break
      #tem que acabar com o jogo aqui

  pg.display.update()