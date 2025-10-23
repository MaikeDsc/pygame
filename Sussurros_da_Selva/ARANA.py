import pygame
from pygame.locals import *

class Arana:
    def __init__(self,x,y,chao_Y,largura):
        self.largura = largura
        self.chao_Y = chao_Y
        self.rect = pygame.Rect(x,y,40,80)
        self.velocidade_x = 7
        self.velocidade_y = 0
        self.gravidade = 1
        self.esta_no_ar = False
        self.direcao = 1

    def desenhar(self, tela):
        
        pygame.draw.rect(tela, (255, 0, 0), self.rect)
        

    def atualizar(self):
        if self.esta_no_ar:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y
            

        if self.rect.bottom >= self.chao_Y:
            self.rect.bottom = self.chao_Y
            self.velocidade_y = 0
            self.esta_no_ar = False
    
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