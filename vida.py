#qnd inimigo morre - gera berry, se sprite da berry entrar em contato com o pokemon +1 vida
#qnd se entra em contato com o pokemon, o inimigo tira uma qtd de vida x dele e some da tela
from personagens import *
import pygame as pg
from random import randint

class General(pg.sprite.Sprite):
    def check_collision(sprite: pg.sprite.Sprite, group: pg.sprite.Group):
        """
        sprite parameter: Sprite that will be used for collision checking
        group parameter: group of sprites that will be checked
        This function checks if any sprites from group collide with sprite.
        """
        if pg.sprite.spritecollide(sprite, group, dokill=True):
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


class Enemy(General):
    def enemy_loss(inimigo):
        inimigo.life -= 1
        if inimigo.life < 1:
            inimigo.kill()

class Player(General):
    def player_gain(player):
        if player.life < 3:
            print(player.life)
            player.life += 1 #da para criar berry com poderes diferentes e colocar em condicoes etc.
    
    def player_loss(player):
        player.life -= 1
        if player.life < 1:
            return True

    def player_buff(player):
        player.velocidadeX = 5
        player.intervalo = 250

    def player_nerf(player):
        player.velocidadeX = 3
        player.intervalo = 500
