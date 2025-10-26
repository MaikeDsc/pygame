import pygame
from pygame.locals import *
from sys import exit
from BALAS import *
from ARANA import *
from VILAO import *
from MAGIA import *
from INIMIGOS import *
import os


pygame.init()

def pathabs(*partes):
    dir_atual = os.path.dirname(__file__)

    return os.path.join(dir_atual, *partes)


largura = 1280
altura = 720

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Sussuros da Selva")

cenario_fase1 = pygame.image.load("Sussurros_da_Selva/imagens/fundo/cenario_1.png")

#------------------------- Carregamento de sons ----------------------------------

menu_sound = pygame.mixer.music.load("Sussurros_da_Selva/musica e sons/menu_sound.mp3")
pygame.mixer.music.play(-1)

laser = pygame.mixer.Sound("Sussurros_da_Selva/musica e sons/laser.wav")
laser.set_volume(0.2)

grito_curupira = pygame.mixer.Sound("Sussurros_da_selva/musica e sons/gritos/grito_magia_fogo.mp3")
grito_curupira.set_volume(0.2)

#----------------- POSIÇÕES DO CURUPIRA --------------------------
#posições em x  1 e 2 do Vilão
'''vilao_xposicao_1 = 1000
vilao_xposicao_2 = 20

#para usar no if  
vilao_pos1 = 0
vilao_pos2 = 1
vilao_pos_atual = vilao_pos1

#tempos do Vilão em cada posição ele começa na 1 
tpos_vilao1 = 22800
tpos_vilao2 = 22800
time_inicio_posicao = pygame.time.get_ticks()

#estados do curupira
estado_obsoleto = 0
estado_atacando = 1
estado_atual= estado_obsoleto

#setando os tempo dos ataques 
tempo_obsoleto = 3000    
tempo_lancando = 2400

time_inicio_estado = pygame.time.get_ticks()
  '''

#--------------------------- INSTÂNCIAS ---------------------------

chao_Y = 625
x_arana = 100
y_arana = 550
arana = Arana(x_arana,y_arana,chao_Y,largura)

x_curupira = 1100
y_curupira = 520
curupira = Vilao('curupira', x_curupira, y_curupira, 1.7, tela)

bola1 = Magias('bola_de_fogo',1400, 300, 2.5, 10, tela )   #parametros : nome pasta de imagens, pos x, po y, escala, velocidade
bola2 = Magias('bola_de_fogo',1400, 590, 2.5, 10, tela )

rato1 = Inimigos('rato',-200, 605, 0.5, 1, 'direita', tela  )         
capivara = Inimigos('capivara', 1300, 583, 3, 4,'esquerda', tela)


projeteis = []

clock = pygame.time.Clock()

BRANCO = (255,255,255)
PRETO = (0,0,0)


def resetar_fase1():
    global arana, curupira, bola1, bola2, rato1, capivara, projeteis, x_curupira,y_curupira,x_arana,y_arana
    global tempo_fase1, vilao_pos1, vilao_pos2, vilao_pos_atual
    global time_inicio_posicao, tpos_vilao1, tpos_vilao2, vilao_xposicao_1,vilao_xposicao_2
    global estado_obsoleto, estado_atacando, estado_atual
    global tempo_obsoleto, tempo_lancando, time_inicio_estado

    tempo_fase1 = pygame.time.get_ticks()

    #recriar personagens
    arana = Arana(x_arana,y_arana,chao_Y,largura, 3)
    curupira = Vilao('curupira', x_curupira, y_curupira, 1.7, tela)
    curupira.vivo = True

    bola1 = Magias('bola_de_fogo',1400, 300, 2.5, 10, tela )  
    bola2 = Magias('bola_de_fogo',1400, 590, 2.5, 10, tela )

    rato1 = Inimigos('rato',-200, 605, 0.5, 1, 'direita', tela  )         
    capivara = Inimigos('capivara', 1300, 583, 3, 4,'esquerda', tela)

    projeteis = []

    #estados do vilao e temporizadores
    vilao_xposicao_1 = 1000
    vilao_xposicao_2 = 20

    #para usar no if  
    vilao_pos1 = 0
    vilao_pos2 = 1
    vilao_pos_atual = vilao_pos1

    #tempos do Vilão em cada posição ele começa na 1 
    tpos_vilao1 = 22800
    tpos_vilao2 = 22800
    time_inicio_posicao = tempo_fase1

    #estados do curupira
    estado_obsoleto = 0
    estado_atacando = 1
    estado_atual= estado_obsoleto

    #setando os tempo dos ataques 
    tempo_obsoleto = 3000    
    tempo_lancando = 2400

    time_inicio_estado = tempo_fase1

def intro():
    pasta_frames = pathabs('imagens','intro')
    fps = 20

    frames = []

    for nome in sorted(os.listdir(pasta_frames)):
        if nome.endswith('.png'):
            caminho = os.path.join(pasta_frames,nome)
            imagem = pygame.image.load(caminho).convert()
            imagem = pygame.transform.scale(imagem, (largura, altura))

            frames.append(imagem)

    frame_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        tela.blit(frames[frame_index], (0,0))
        pygame.display.flip()

        frame_index += 1

        if frame_index >= len(frames):
            return 'submenu'
        
        clock.tick(fps)

def submenu():
    pasta_frames = pathabs('imagens','submenu')
    fps = 25

    frames = []

    for nome in sorted(os.listdir(pasta_frames)):
        if nome.endswith('.png'):
            caminho = os.path.join(pasta_frames,nome)
            imagem = pygame.image.load(caminho).convert()
            imagem = pygame.transform.scale(imagem, (largura, altura))

            frames.append(imagem)

    frame_index = 0

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                return 'menu'

        tela.blit(frames[frame_index], (0,0))
        pygame.display.flip()

        frame_index += 1

        if frame_index >= len(frames):
            frame_index = 0
        
        clock.tick(fps)

def menu():
    pasta_frames = pathabs('imagens','menu')
    fps = 25

    frames = []

    for nome in sorted(os.listdir(pasta_frames)):
        if nome.endswith('.png'):
            caminho = os.path.join(pasta_frames,nome)
            imagem = pygame.image.load(caminho).convert()
            imagem = pygame.transform.scale(imagem, (largura, altura))

            frames.append(imagem)

    frame_index = 0

    while True:

        jogar = pygame.draw.rect(tela,'white',(538,385,205,57))
        tutorial = pygame.draw.rect(tela,'white',(538,469,205,57))
        sair = pygame.draw.rect(tela,'white',(538,551,205,57))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if jogar.collidepoint(event.pos):
                    resetar_fase1()
                    return 'fase 1'
                
                elif sair.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        tela.blit(frames[frame_index], (0,0))
        
        pygame.display.flip()

        frame_index += 1

        if frame_index >= len(frames):
            frame_index = 0
        
        clock.tick(fps)


estado = "menu"
tempo_total = 90


while True:
    if estado == "intro":
        estado = intro()

    elif estado == "submenu":
        estado = submenu()

    elif estado == "menu":

      estado = menu()
                    
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

        if arana.rect.colliderect(bola1.rect) or arana.rect.colliderect(bola2.rect):
            arana.tomar_dano()
            if arana.vivo == False:
                estado = 'game over'
        
        teclas = pygame.key.get_pressed()
        arana.movimento(teclas)


        #--------------------PERSONAGENS E ATAQUES---------------------------------
        arana.atualizar()
        arana.desenhar(tela)

        bola1.atualizar_animacao()
        bola2.atualizar_animacao()
        curupira.atualizar_animacao()         #atualiza o frame antes de desenhar
        curupira.draw()                       #desenhar as imagem com o metodo draw

        #------------------- CURUPIRA -------------------------------------

        time_atual = pygame.time.get_ticks() 

        if curupira.vivo == True:

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
                grito_curupira.play()

                if vilao_pos_atual == vilao_pos1:
                    
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
                        bola1.rect.x = 1300
                        bola2.rect.x = 1300       
                
                if vilao_pos_atual == vilao_pos2:
                   
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
         
        #----------------------------- outros inimigos ------------------------

        #-----------primeiro rato    ---------------------
        if time_atual - tempo_fase1 > 6000:

            rato1.atualizar_animacao()
            rato1.draw()
            rato1.movimento()   
            
            if rato1.rect.x < -150 :   
                rato1.direcao = "direita"

            elif rato1.rect.x > 1200: 
                rato1.direcao = "esquerda"

        #---------------capivara ----------------------  
        if time_atual - tempo_fase1 > 30000:

            capivara.atualizar_animacao()
            capivara.draw()
            capivara.movimento()
             
            if capivara.rect.x < -150 :   
                capivara.direcao = "direita"

            elif capivara.rect.x > 1200: 
                capivara.direcao = "esquerda"

        #---------------------COLIZOES DOS PROJETEIS DO ARANA ------------------
        for bala in projeteis:
            bala.atualizar()
            bala.desenhar()

            if bala.rect.x > largura or bala.rect.x < 0:
                projeteis.remove(bala)
            elif curupira.vivo and bala.rect.colliderect(curupira.rect):
                curupira.tomar_dano()
                projeteis.remove(bala)

        pygame.display.flip()

#------------------------------ GAME OVER ---------------------------------------------------------

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
                #pygame.mixer.music.stop()
                #pygame.mixer.music.load("Sussurros_da_Selva/musica e sons/menu_sound.mp3")
                #pygame.mixer.music.play(-1)
                estado = "menu"
