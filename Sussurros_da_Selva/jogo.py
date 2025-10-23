import pygame
from pygame.locals import *
from sys import exit
from BALAS import *
from ARANA import *
from VILAO import *
from MAGIA import *
from INIMIGOS import *
from moviepy import VideoFileClip


def pathabs(pasta,arquivo):

    import os

    dir_atual = os.path.dirname(__file__)

    return os.path.join(dir_atual,pasta,arquivo)

pygame.init()



largura = 1280
altura = 720

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Sussuros da Selva")

cenario_fase1 = pygame.image.load("Sussurros_da_Selva/imagens/fundo/cenario_1.png")

#parte sonora

menu_sound = pygame.mixer.music.load("Sussurros_da_Selva/musica e sons/menu_sound.mp3")
pygame.mixer.music.play(-1)

laser = pygame.mixer.Sound("Sussurros_da_Selva/musica e sons/laser.wav")
laser.set_volume(0.2)

#posições em x  1 e 2 do Vilão
vilao_xposicao_1 = 800
vilao_xposicao_2 = 20

#para usar no if  
vilao_pos1 = 0
vilao_pos2 = 1
vilao_pos_atual = vilao_pos1
#tempos do Vilão em cada posição ele começa na 1 

tpos_vilao1 = 30000
tpos_vilao2 = 20000

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

#define a instancia player 

chao_Y = 625

x_arana = 100
y_arana = 550

x_curupira = 1100
y_curupira = 520

curupira = Vilao('curupira', x_curupira, y_curupira, 1.7, tela)

arana = Arana(x_arana,y_arana,chao_Y,largura)

bola1 = Magias('bola_de_fogo',1050, 350, 2.5, 10, tela )              #parametros : nome pasta de imagens, pos x, po y, escala, velocidade
bola2 = Magias('bola_de_fogo',1050, 590, 2.5, 10, tela )

# rato1 = Inimigos('rato',1100, 598, 0.5, 1, tela  )         

# capivara = Inimigos('capivara', 1100, 580, 3, 4, tela)


#-----------------------------------------------------------------------------

projeteis = []

clock = pygame.time.Clock()

fonte_menu = pygame.font.Font("Sussurros_da_Selva/fonte_de_texto/PressStart2P.ttf", 35)
BRANCO = (255,255,255)
PRETO = (0,0,0)

def desenhar_texto(texto,fonte,cor,y):
    img = fonte.render(texto,True,cor)
    x = (largura - img.get_width()) // 2
    tela.blit(img,(x,y))

def intro_video(tela,largura,altura):
    
    clip = VideoFileClip(pathabs("videos","intro.mp4")).resized((largura,altura))
    
    for frame in clip.iter_frames(fps = 30, dtype = "uint8"):
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        tela.blit(frame_surface, (0,0))
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    clip.close()
    return "introducao"

def introducao(tela,largura,altura):
    clip = VideoFileClip(pathabs("introducao","introducao_2.mp4")).resized((largura,altura))
    
    for frame in clip.iter_frames(fps = 30, dtype = "uint8"):
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        tela.blit(frame_surface, (0,0))
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    clip.close()
    return 'menu'

estado = "menu"

tempo_total = 30

while True:
    if estado == "intro":
        estado = intro_video(tela,largura,altura)

    elif estado == "introducao":
        estado = introducao(tela,largura,altura)

    elif estado == "menu":

        tela.fill(PRETO)

        desenhar_texto("SUSSUROS DA SELVA",fonte_menu, BRANCO, 200)
        desenhar_texto("Pressione ENTER para jogar", fonte_menu, BRANCO, 400)
        desenhar_texto("Pressione ESC para sair", fonte_menu, BRANCO, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Sussurros_da_Selva/musica e sons/trilha sonora fase 1.mp3")
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(-1)
                    tempo_fase1 = pygame.time.get_ticks()
                    estado = "fase 1"

                if event.key == K_ESCAPE:
                    
                    exit()

                    
    elif estado == "fase 1":

        clock.tick(60)
        tela.blit(cenario_fase1, (0,0))

        tempo_decorrido = (pygame.time.get_ticks() - tempo_fase1) / 1000  # em segundos

        tempo_restante = max(0, tempo_total - tempo_decorrido)
        
        minutos = int(tempo_restante // 60)
        segundos = int(tempo_restante % 60)
        texto_tempo = f"{minutos:02d}:{segundos:02d}"

        fonte_cronometro = pygame.font.Font("Sussurros_da_Selva/fonte_de_texto/PressStart2P.ttf", 35)
        texto_cronometro = fonte_cronometro.render(texto_tempo, True, (255,255,255))
        tela.blit(texto_cronometro, (600, 110))

        if tempo_restante <= 0:
            estado = "game over"

        #movimentos do jogo aqui embaixo
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_o:
                    laser.play()
                    nova_bala = Balas(arana.rect.right, arana.rect.centery, arana.direcao,tela)
                    projeteis.append(nova_bala) 
        
        teclas = pygame.key.get_pressed()
        arana.movimento(teclas)

        #personagens e ataques

        curupira.atualizar_animacao()         #atualiza o frame antes de desenhar
        bola1.atualizar_animacao()
        bola2.atualizar_animacao()

        #rato1.atualizar_animacao()
        #capivara.atualizar_animacao()
    
        curupira.draw()                       #desenhar as imagem com o metodo draw
    
        #rato1.draw()
        #rato1.movimento()

        #capivara.draw()
        #capivara.movimento()
        
        time_atual = pygame.time.get_ticks() - tempo_fase1

        if vilao_pos_atual == vilao_pos1: #------------------ aqui vai para a segunda posição
            if time_atual - time_inicio_posicao >= tpos_vilao1:
                curupira.giro = True
                curupira.rect.x = vilao_xposicao_2
                vilao_pos_atual = vilao_pos2
                time_inicio_posicao = time_atual
        
        if vilao_pos_atual == vilao_pos2:               #aqui volta para a posicao inicial 
            if time_atual - time_inicio_posicao >= tpos_vilao2:
                curupira.giro = False
                curupira.rect.x = vilao_xposicao_1
                vilao_pos_atual = vilao_pos1
                time_inicio_posicao = time_atual


        if estado_atual == estado_obsoleto:
            if time_atual - time_inicio_estado >= tempo_obsoleto:
                estado_atual = estado_atacando
                curupira.atualizar_acoes(1)
                time_inicio_estado = time_atual

        if estado_atual == estado_atacando:
            if vilao_pos_atual == vilao_pos1 and curupira.vivo == True:
                bola1.giro = False
                bola2.giro = False
                bola1.draw()
                bola1.movimento(0)
                bola2.draw()
                bola2.movimento(0)
            
                if time_atual - time_inicio_estado >= tempo_lancando:
                    estado_atual = estado_obsoleto
                    curupira.atualizar_acoes(0)
                    time_inicio_estado = time_atual

                    #aqui tem q redefinir a posição da bola p poder ela aparecer novamente
                    bola1.rect.x = 1050
                    bola2.rect.x = 1050
            
            if vilao_pos_atual == vilao_pos2 and curupira.vivo == True:
                bola1.giro = True
                bola2.giro = True
                bola1.draw()
                bola1.movimento(1)
                bola2.draw()
                bola2.movimento(1)
            
                if time_atual - time_inicio_estado >= tempo_lancando:
                    estado_atual = estado_obsoleto
                    curupira.atualizar_acoes(0)
                    time_inicio_estado = time_atual

                    #aqui tem q redefinir a posição da bola para ela poder aparecer novamente
                    bola1.rect.x = -150
                    bola2.rect.x = -150
            

        arana.atualizar()
        arana.desenhar(tela)

        for bala in projeteis:
            bala.atualizar()
            bala.desenhar()

            if bala.rect.x > largura or bala.rect.x < 0:
                projeteis.remove(bala)
            elif curupira.vivo and bala.rect.colliderect(curupira.rect):
                curupira.tomar_dano()
                projeteis.remove(bala)

        pygame.display.flip()

#-------------------------------------------------------------------------------------------------

    elif estado == "game over":
        fonte_titulo = pygame.font.Font("Sussurros_da_Selva/fonte_de_texto/PressStart2P.ttf", 50)
        fonte_texto = pygame.font.Font("Sussurros_da_Selva/fonte_de_texto/PressStart2P.ttf", 20)

        texto_game_over = fonte_titulo.render("GAME OVER", True, (255,0,0) )
        texto_voltar = fonte_texto.render("Toque em qualquer botao para voltar ao menu", True, BRANCO)

        tela.fill(PRETO)

        tela.blit(texto_game_over, (largura//2 - texto_game_over.get_width()//2, altura//3))
        tela.blit(texto_voltar, (largura//2 - texto_voltar.get_width()//2, altura//2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Sussurros_da_Selva/musica e sons/menu_sound.mp3")
                pygame.mixer.music.play(-1)
                estado = "menu"