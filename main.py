import pygame as pg
from sys import exit
from personagens import *
from acoes import *


pg.init()

#Aqui criamos os sons de efeitos especias
som_de_item = pg.mixer.Sound("Sounds/item.wav")
som_de_item.set_volume(0.1)
som_de_vida = pg.mixer.Sound("Sounds/vida.wav")
som_de_vida.set_volume(0.1)
som_perde_vida = pg.mixer.Sound("Sounds/perder-vida.wav")
som_perde_vida.set_volume(0.1)
som_acerta_tiro = pg.mixer.Sound("Sounds/acertar-tiro.wav")
som_acerta_tiro.set_volume(0.02)

#Aqui criamos a musica de fundo
pg.mixer.music.set_volume(0.06)
musica_de_fundo = pg.mixer.music.load("Sounds/music.mp3")
pg.mixer.music.play(-1)

#Aqui criamos o relogio
clock = pg.time.Clock()


font = pg.font.SysFont("arial",30)
pontos = 0
tempo_atual = 0

#Aqui definimos a largura e altura da tela
largura, altura = 600, 720

#Aqui criamos a tela
tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('PokeFall')

inimigos = pg.sprite.Group()
pikachu = Pikachu(110,110, largura, altura, tela)

berries = pg.sprite.Group()
item = pg.sprite.Group()
bala = pg.sprite.Group()
  
background = pg.image.load("Assets/background.jpeg")

#Aqui começa o jogo
while True:
  mensagem = f"{pontos}"
  pontuacao = font.render(mensagem, False, "WHITE")

  #Aqui checamos se o usuario clicou no X para fechar o jogo
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()
  
  #Aqui adicionamos os inimigos na tela
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
  if "F" not in lista_depok and pontos >= 50:
    inimigos.add(Farfetch(80, 80, largura, altura, tela, som_perde_vida))
  if "P" not in lista_depok and pontos >= 150:
    inimigos.add(Pidgeot(100, 100, largura, altura, tela, som_perde_vida))
  if "Z" not in lista_depok:
    inimigos.add(Zubat(60, 60, largura, altura, tela, som_perde_vida))
  if "D" not in lista_depok and pontos >= 500:
    inimigos.add(Dragonite(160, 160, largura, altura, tela, som_perde_vida))
  

  tela.blit(background,(0,0))
  tela.blit(pontuacao, (30, 30))
  tempo = pg.time.get_ticks()

  #Botamos o pikachu na tela
  pikachu.draw()
  pikachu.update(bala, tempo)

  #Checamos a pontuação
  pontos = soma_pontos(0)

  inimigos.update(bala, berries, pikachu, item, som_acerta_tiro)
  inimigos.draw(tela)

  #Checamos a vida do pikachu
  if pikachu.life == 3:
    imagem = pg.transform.scale(pg.image.load("Assets/3-HP.png"), (100, 40))
    tela.blit(imagem, (largura-110,10))

  elif pikachu.life == 2:
    imagem = pg.transform.scale(pg.image.load("Assets/2-HP.png"), (100, 40))
    tela.blit(imagem, (largura-110,10))
  else:
    imagem = pg.transform.scale(pg.image.load("Assets/1-HP.png"), (100, 40))
    tela.blit(imagem, (largura-110,10))

  berries.update()
  berries.draw(tela)

  item.update()
  item.draw(tela)
  
  bala.update()
  bala.draw(tela)

  #para padronizar o fps
  fps = font.render(str(int(clock.get_fps())),True,"WHITE")
  clock.tick(60)

  #checa colisao entre pikachu e o item que recupera vida
  if General.check_collision(pikachu, berries):
    som_de_vida.play()
    Player.player_gain(pikachu)
  
  #checa colisao entre pikachu e o item que buffa o pikachu
  if General.check_collision(pikachu, item):
    Player.player_buff(pikachu)
    som_de_item.play()
    tempo_atual = pg.time.get_ticks()
  
  #nerfa o pikachu depois do tempo estimado
  if tempo >= tempo_atual + 5000:
    Player.player_nerf(pikachu)

  #checa colisao entre pikachu e os inimigos
  if General.check_collision(pikachu, inimigos):
    som_perde_vida.play()
    if Player.player_loss(pikachu):
      break
      #Aqui acaba o jogo

  pg.display.update()