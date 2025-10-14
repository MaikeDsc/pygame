import pygame

class Balas:
    def __init__(self,x,y,direcao,tela):
        self.tela = tela
        if direcao == 1:
            self.rect = pygame.Rect(x,y,40,2)
        else:
            self.rect = pygame.Rect(x - 80 ,y,40,2)
        
        self.velocidade = 15 * direcao
    
    def atualizar(self):
        self.rect.x += self.velocidade
    
    def desenhar(self):
        pygame.draw.rect(self.tela, (255,255,255),self.rect)