import pygame
from vilao import Vilao
from vilao import Projeteis

import pygame

pygame.init()

largura = 900
altura = int(largura * 0.7)   
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('vilão')

#taxas de quadro (frame rate)
relogio = pygame.time.Clock()
fps = 60


#carregando u a imagem para o bg
imagem_fundo = pygame.image.load('sussurus/imagens/fundo/selva2.png')
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura,altura))

#posições em x  1 e 2 do Vilão
vilao_posicao_1 = 780
vilao_posicao_2 = 200
#para usar no if  
vilao_pos1 = 0
vilao_pos2 = 1
vilao_pos_atual = vilao_pos1

#tempos do Vilão em cada posição ele começa na 1 
tpos_vilao1 = 10000
tpos_vilao2 = 8000

time_inicio_posicao = pygame.time.get_ticks()

#estados do curupira
estado_obsoleto = 0
estado_atacando = 1
estado_atual= estado_obsoleto
#setando os tempo dos ataques 
tempo_obsoleto = 3000    #em milisegundos pq o relogio só conta em milisegundos
tempo_lancando = 2400

time_inicio_estado = pygame.time.get_ticks()


#--------------------------------------------------------------------------------

#função para desenhar o fundo
def desenhar_bg():
    tela.blit(imagem_fundo, (0,0))

  
#--------------------------------------------------------------------------------

#define a instancia player 
curupira = Vilao('curupira', vilao_posicao_1, 475, 1.7, tela)

bola1 = Projeteis('curupira',900, 300, 2.5, 10, tela )              #parametros : nome pasta de imagens, pos x, po y, escala, velocidade
bola2 = Projeteis('curupira',900, 500, 2.5, 10, tela )          





loop = True
while loop:

    relogio.tick(fps)

    desenhar_bg()                       #backgrownd

    curupira.atualizar_animacao()         #atualiza o frame antes de desenhar
    bola1.atualizar_animacao()
    bola2.atualizar_animacao()
    #bola3.atualizar_animacao()
    
    curupira.draw()                       #desenhar as imagem com o metodo draw
   
    

    for event in pygame.event.get():

        #eventos de usuario
        if event.type == pygame.QUIT:
            loop = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False


    time_atual = pygame.time.get_ticks()

    #if vilao_pos_atual == vilao_pos1 ------------------definir o teleport aqui 
    


    if estado_atual == estado_obsoleto:
        if time_atual - time_inicio_estado >= tempo_obsoleto:
            estado_atual = estado_atacando
            curupira.atualizar_acoes(1)
            time_inicio_estado = time_atual

    if estado_atual == estado_atacando:
        
        bola1.draw()
        bola1.movimento()
        bola2.draw()
        bola2.movimento()
       
        if time_atual - time_inicio_estado >= tempo_lancando:
            estado_atual = estado_obsoleto
            
            curupira.atualizar_acoes(0)
            time_inicio_estado = time_atual

            #aqui tem q redefinir a posição da bola p poder ela aparecer novamente
            bola1.rect.x = 900
            bola2.rect.x = 900
    
    pygame.display.update()
pygame.quit()