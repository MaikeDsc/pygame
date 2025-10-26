import pygame
from pygame.locals import *

class Arana:
    def __init__(self,x,y,chao_Y,largura,vida = 3):
        self.vida = vida
        self.vivo = True

        self.largura = largura
        self.chao_Y = chao_Y
        self.rect = pygame.Rect(x,y,40,80)
        self.velocidade_x = 7
        self.velocidade_y = 0
        self.gravidade = 1
        self.esta_no_ar = False
        self.direcao = 1

        self.invulneravel = False
        self.tempo_ultimo_dano = 0
        self.tempo_invulnerabilidade = 3000
        self.intervalo_piscar = 100
        self.mostrar_sprite = True

    def desenhar(self, tela):

        if self.mostrar_sprite == True:
            pygame.draw.rect(tela, (255, 0, 0), self.rect)
        

    def atualizar(self):
        if self.esta_no_ar:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y
            

        if self.rect.bottom >= self.chao_Y:
            self.rect.bottom = self.chao_Y
            self.velocidade_y = 0
            self.esta_no_ar = False

        tempo_atual = pygame.time.get_ticks()

        if self.invulneravel == True:
            if (tempo_atual - self.tempo_ultimo_dano) // self.intervalo_piscar % 2 == 0:
                self.mostrar_sprite = False
            else:
                self.mostrar_sprite = True

            if tempo_atual - self.tempo_ultimo_dano >= self.tempo_invulnerabilidade:
                self.invulneravel = False
                self.mostrar_sprite = True
    
    def movimento(self,teclas):
        if teclas[K_a]:
            self.direcao = -1
            self.rect.x -= self.velocidade_x
            if self.rect.x < 0:
                self.rect.x = 0
        if teclas[K_d]:
            self.direcao = 1
            self.rect.x += self.velocidade_x
            if self.rect.x > self.largura - 40:
                self.rect.x = self.largura - 40
        if teclas[K_w]:
            self.pular()

    def pular(self):
        if not self.esta_no_ar:
            self.velocidade_y = -20
            self.esta_no_ar = True

    def tomar_dano(self, dano = 1):

        tempo_atual = pygame.time.get_ticks()

        if self.vivo and self.invulneravel == False:
            self.vida -= dano
            if self.vida == 0:
                self.vivo = False

            self.invulneravel = True
            self.tempo_ultimo_dano = tempo_atual