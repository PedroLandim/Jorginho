#qnd inimigo morre - gera berry, se sprite da berry entrar em contato com o pokemon +1 vida
#qnd se entra em contato com o pokemon, o inimigo tira uma qtd de vida x dele e some da tela
import pygame

class General:
     def check_collision(sprite: pygame.sprite.Sprite, group: pygame.sprite.Group):
        """
        sprite parameter: Sprite that will be used for collision checking
        group parameter: group of sprites that will be checked
        This function checks if any sprites from group collide with sprite.
        """
        if len(pygame.sprite.spritecollide(sprite, group, dokill=True)):
            return True
        return False


class Enemy(General):

    def enemy_dies(self):
        #nesse caso o inimigo sempre morre com um tiro, mas da para randomizar o dano
        self.life = 0
        self.kill()
        #gerar berry

    if General.check_collision(enemy, bullet):
        enemy_dies()



class Player(General):
    def is_dead(self): #esse parametro possivelmente vai para o General qnd a gente randomizar as berries e os pokemons
        '''
        This method checks if the player life has reached zero.
        '''
        if self.life <1:
            return True
        else:
            return False

    if General.check_collision(player, berry):
        player.life += 1 #da para criar berry com poderes diferentes e colocar em condicoes etc.
    
    if General.check_collision(player, enemy):
        player.life -= 1
        is_dead()
    
    if is_dead():
        player.kill()
        #e tem que acabar o jogo