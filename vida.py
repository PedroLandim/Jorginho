#qnd inimigo morre - gera berry, se sprite da berry entrar em contato com o pokemon +1 vida
#qnd se entra em contato com o pokemon, o inimigo tira uma qtd de vida x dele e some da tela
from movimentos import Pikachu
import pygame as pg
from random import randint

#rrrr
class Bala(pg.sprite.Sprite):
    def __init__(self, windowWidth, windowHeight, width):
        pg.sprite.Sprite.__init__(self)
        self.ImagemBala = pg.image.load('assets/relampago.png')

        self.rect = self.imagemBala.get.rect()
        self.velocidadeBala = 5

        #nao sei se essa posicao ta certa
        self.rect.top = windowHeight
        self.rect.left = windowWidth/2 - width/2

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala


#rrr

class General(pg.sprite.Sprite):
    def check_collision(sprite: pg.sprite.Sprite, group: pg.sprite.Group):
        """
        sprite parameter: Sprite that will be used for collision checking
        group parameter: group of sprites that will be checked
        This function checks if any sprites from group collide with sprite.
        """
        if len(pg.sprite.spritecollide(sprite, group, dokill=True)):
            return True
        return False

    def is_dead(self):
        '''
        This method checks if the player life has reached zero.
        '''
        if self.life <1:
            return True
        else:
            return False

class Berry(pg.sprite.Sprite):
    #responsável por criar as berries
    def __init__(self, windowWidth, windowHeight, tela, pokemonX, pokemonY):
                super().__init__()
                self.width = 60
                self.height = 60
                self.image = pg.transform.scale(pg.image.load('assets/berry.png'), (self.width, self.height))
                self.velocidadeY = 1
                self.windowWidth = windowWidth
                self.windowHeight = windowHeight
                self.x = pokemonX
                self.y = pokemonY
                self.tela = tela
                self.rect = self.image.get_rect()
                self.life = 3
            
    def draw(self):
        #desenha a imagem na tela do jogo.
        self.tela.blit(self.image, (self.x,self.y))

    def update(self):
        # movimenta o pokemon de acordo com a velocidade.
        self.y += self.velocidadeY
        if self.y >= self.windowHeight:
            self.y = -self.height
        self.x = randint(0, self.windowWidth-self.width)
        self.rect.topleft = (self.x,self.y)



class Enemy(General):
    
    def enemy_loss(inimigo):
        inimigo.life -= 1


class Player(General):

    def player_gain(player):
        if player.life < 3:
            player.life += 1 #da para criar berry com poderes diferentes e colocar em condicoes etc.
    
    def player_loss(player):
        player.life -= 1
        if General.is_dead(player):
            Pikachu.kill()