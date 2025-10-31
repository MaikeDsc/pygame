import pygame

class Balas:
    def __init__(self,x,y,direcao,tela):
        pygame.sprite.Sprite.__init__(self)
        self.tela = tela
        self.giro = False
        self.dardo = pygame.image.load(f'Sussurros_da_Selva/imagens/arana/dardo/dardo.png')
        self.rect = self.dardo.get_rect()
        self.rect.center = (x, y)
        
        
        if direcao == 1:
            self.giro = True
        else:
            self.giro = False

        
        self.velocidade = 15 * direcao
    
    def atualizar(self):
        self.rect.x += self.velocidade
    
    def desenhar(self):
        self.tela.blit(pygame.transform.flip(self.dardo, self.giro, False) ,self.rect)