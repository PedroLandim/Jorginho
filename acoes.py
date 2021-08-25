from personagens import *
import pygame as pg
from random import randint

class General(pg.sprite.Sprite):
    def check_collision(sprite: pg.sprite.Sprite, group: pg.sprite.Group):
        """
        parametro da sprite: Sprite que vai ser usada para checar colisões
        parametro do grupo: grupo de sprites que vai ser checado
        Essa função checa se uma sprite de um grupo colide com uma outra sprite.
        """
        if pg.sprite.spritecollide(sprite, group, dokill=True):
            return True
        return False

    def is_dead(self):
        #Essa função checa se a vida do personagem chegou a zero
        if self.life <1:
            return True
        else:
            return False


#Checa se o inimigo perdeu vida/morreu
class Enemy(General):
    def enemy_loss(inimigo):
        inimigo.life -= 1
        if inimigo.life < 1:
            inimigo.kill()

class Player(General):
    #Checa se o pikachu vai ganhar vida
    def player_gain(player):
        if player.life < 3:
            player.life += 1
    
    #Checa se o pikachu perdeu vida/morreu
    def player_loss(player):
        player.life -= 1
        if player.life < 1:
            return True

    #Buffa o pikachu
    def player_buff(player):
        player.velocidadeX = 5
        player.intervalo = 250

    #Nerfa o pikachu
    def player_nerf(player):
        player.velocidadeX = 3
        player.intervalo = 500
