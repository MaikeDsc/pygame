import pygame
from pygame.locals import *
from sys import exit
from BALAS import *
from ARANA import *
from VILAO import *
from MAGIA import *
from INIMIGOS import *
import os

pygame.mixer.pre_init(44100, -16, 2, 128)
pygame.init()
pygame.mixer.set_num_channels(16)

def pathabs4(*partes):
    dir_atual = os.path.dirname(__file__)

    return os.path.join(dir_atual, *partes)


largura = 1280
altura = 720

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Sussuros da Selva")

cenario_fase1 = pygame.image.load(pathabs4("imagens/fundo/cenario_1.png"))

barra_vida_arana = pygame.image.load(pathabs4("imagens/hud/tronco/0.png"))
barra_vida_arana = pygame.transform.scale(barra_vida_arana, (300,200))

ponto_de_vida = pygame.image.load(pathabs4("imagens/hud/folha/1.png"))
ponto_de_vida = pygame.transform.scale(ponto_de_vida, (250,150))

ponto_de_vida_nulo = pygame.image.load(pathabs4("imagens/hud/folha/0.png"))
ponto_de_vida_nulo = pygame.transform.scale(ponto_de_vida_nulo, (250,150))

#------------------------- Carregamento de sons ----------------------------------

pygame.mixer.music.load(pathabs4("musica e sons/menu_sound.mp3"))
pygame.mixer.music.play(-1)

click = pygame.mixer.Sound(pathabs4("musica e sons/click.wav"))
click.set_volume(0.6)

dardo = pygame.mixer.Sound(pathabs4("musica e sons/dardo.wav"))
dardo.set_volume(0.6)

grito_curupira = pygame.mixer.Sound(pathabs4("musica e sons/gritos/grito_magia_fogo.wav"))
grito_curupira.set_volume(0.15)

def tocar_som(som):
    canal = pygame.mixer.find_channel(True)
    canal.play(som)

#--------------------------- INSTÂNCIAS ---------------------------

chao_Y = 637
x_arana = 100
y_arana = 562

arana = Arana('Arana',x_arana,y_arana,2,chao_Y,largura, 3)

x_curupira = 1100
y_curupira = 520

bola1 = Magias('bola_de_fogo',1400, 280, 2.5, 10, tela )   #parametros : nome pasta de imagens, pos x, po y, escala, velocidade
bola2 = Magias('bola_de_fogo',1400, 590, 2.5, 10, tela )

rato = Inimigos('rato',-200, 610, 0.4, 7, 'direita', tela )         
capivara = Inimigos('capivara', 1300, 589, 2.5, 6.5,'esquerda', tela)

portal = Magias('portal1', (largura/2), (altura/2), 2.5, 10, tela)
projeteis = []

clock = pygame.time.Clock()


BRANCO = (255,255,255)
PRETO = (0,0,0)


def resetar_fase1():
    global arana, curupira, bola1, bola2, rato, capivara, projeteis, portal, x_curupira,y_curupira,x_arana,y_arana
    global tempo_fase1, vilao_pos1, vilao_pos2, vilao_pos_atual
    global time_inicio_posicao, tpos_vilao1, tpos_vilao2, vilao_xposicao_1,vilao_xposicao_2
    global estado_obsoleto, estado_atacando, estado_atual
    global tempo_obsoleto, tempo_lancando, time_inicio_estado
    global tempo_congelado


    tempo_congelado = False
    tempo_fase1 = pygame.time.get_ticks()

    #recriar personagens
    arana = Arana('Arana',x_arana,y_arana,2,chao_Y,largura, 3)
    curupira = Vilao('curupira', x_curupira, y_curupira, 1.7, tela)

    bola1 = Magias('bola_de_fogo',1400, 280, 2.5, 10, tela )  
    bola2 = Magias('bola_de_fogo',1400, 590, 2.5, 10, tela )

    rato = Inimigos('rato',-200, 610, 0.4, 7, 'direita', tela  )         
    capivara = Inimigos('capivara', 1300, 589, 2.5, 6.5,'esquerda', tela)
    
    portal = Magias('portal1',(largura/2), (altura/2), 3, 10, tela, 6)

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
    pasta_frames = pathabs4('imagens','intro')
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
    pasta_frames = pathabs4('imagens','submenu')
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
                click.play()
                return 'menu'

        tela.blit(frames[frame_index], (0,0))
        pygame.display.flip()

        frame_index += 1

        if frame_index >= len(frames):
            frame_index = 0
        
        clock.tick(fps)

def menu():
    pasta_frames = pathabs4('imagens','menu')
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
        tutorial_e_dicas = pygame.draw.rect(tela,'white',(538,469,205,57))
        sair = pygame.draw.rect(tela,'white',(538,551,205,57))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if jogar.collidepoint(event.pos):
                    click.play()
                    pygame.mixer.music.load(pathabs4("musica e sons/Nameless King.mp3"))
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                    resetar_fase1()
                    return 'fase 1'
                
                elif sair.collidepoint(event.pos):
                    click.play()
                    pygame.quit()
                    exit()

                elif tutorial_e_dicas.collidepoint(event.pos):
                    click.play()
                    return 'tutorial_1'
                
        tela.blit(frames[frame_index], (0,0))
        
        pygame.display.flip()

        frame_index += 1

        if frame_index >= len(frames):
            frame_index = 0
        
        clock.tick(fps)

def tutorial_1():
    img = pygame.image.load(pathabs4('imagens', 'tutorial', '1.png'))
    arana_correndo = pygame.image.load(pathabs4('imagens', 'arana', 'arana_correndo', '1.png'))
    arana_correndo = pygame.transform.scale(arana_correndo, (125,170))
    arana_pulando = pygame.image.load(pathabs4('imagens', 'arana', 'arana_pulando', '3.png'))
    arana_pulando = pygame.transform.scale(arana_pulando, (125,163))
    arana_atirando = pygame.image.load(pathabs4('imagens', 'arana', 'arana_atirando_parado', '0.png'))
    arana_atirando = pygame.transform.scale(arana_atirando, (125,163))



    while True:

        sair = pygame.draw.rect(tela,'white',(910,651,149,37))
        proximo = pygame.draw.rect(tela,'white',(1089,651,149,37))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if sair.collidepoint(event.pos):
                    click.play()
                    return 'menu'
                
                elif proximo.collidepoint(event.pos):
                    click.play()
                    return 'tutorial_2'

        tela.blit(img, (0,0))
        tela.blit(pygame.transform.flip(arana_correndo,True,False), (127,320))
        tela.blit(arana_correndo, (430,320))
        tela.blit(arana_pulando, (733,315))
        tela.blit(arana_atirando, (1036,315))

        pygame.display.flip()

def tutorial_2():
    img = pygame.image.load(pathabs4('imagens', 'tutorial', '2.png'))
    capivara_tutorial = Inimigos('capivara', largura/2 , altura/2 , 4, 0,'esquerda', tela)

    while True:
        
        sair = pygame.draw.rect(tela,'white',(910,651,149,37))
        voltar = pygame.draw.rect(tela,'white',(1089,651,149,37))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if sair.collidepoint(event.pos):
                    click.play()
                    return 'menu'
                
                elif voltar.collidepoint(event.pos):
                    click.play()
                    return 'tutorial_1'

        tela.blit(img, (0,0))
        capivara_tutorial.atualizar_animacao()
        capivara_tutorial.draw()
        pygame.display.flip()

estado = "menu"
tempo_total = 90
tempo_congelado = False

while True:
    if estado == "intro":
        estado = intro()

    elif estado == "submenu":
        estado = submenu()

    elif estado == "menu":
      estado = menu()

    elif estado == 'tutorial_1':
        estado = tutorial_1()
    
    elif estado == 'tutorial_2':
        estado = tutorial_2()
                    
    elif estado == "fase 1":
        
        
        clock.tick(60)
        tela.blit(cenario_fase1, (0,0))
        tela.blit(barra_vida_arana, (90,30))
        if arana.vida == 3:
            tela.blit(ponto_de_vida, (80,60))
            tela.blit(ponto_de_vida, (130,60))
            tela.blit(ponto_de_vida, (180,60))
        elif arana.vida == 2:
            tela.blit(ponto_de_vida, (80,60))
            tela.blit(ponto_de_vida, (130,60))
            tela.blit(ponto_de_vida_nulo, (180,60))
        elif arana.vida == 1:
            tela.blit(ponto_de_vida, (80,60))
            tela.blit(ponto_de_vida_nulo, (130,60))
            tela.blit(ponto_de_vida_nulo, (180,60))

        if tempo_congelado == True:
            tempo_decorrido = tempo_decorrido
        else:
            tempo_decorrido = (pygame.time.get_ticks() - tempo_fase1) / 1000  # em segundos

        tempo_restante = max(0, tempo_total - tempo_decorrido)
        
        minutos = int(tempo_restante // 60)
        segundos = int(tempo_restante % 60)
        texto_tempo = f"{minutos:02d}:{segundos:02d}"

        fonte_cronometro = pygame.font.Font(pathabs4("fonte_de_texto/PressStart2P.ttf"), 35)
        texto_cronometro = fonte_cronometro.render(texto_tempo, True, (255,255,255))
        tela.blit(texto_cronometro, (600, 110))

        if tempo_restante <= 0:
            pygame.mixer.music.load(pathabs4('musica e sons','trilha_sonora_game_over.mp3'))
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)
            estado = "game over"

        #movimentos do jogo aqui embaixo
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_o:
                    arana.atirar()
                    tocar_som(dardo)
                    if arana.direcao == 1:
                        nova_bala = Balas(arana.rect.right, arana.rect.centery - 25, arana.direcao,tela)
                    else:
                        nova_bala = Balas(arana.rect.left, arana.rect.centery - 25, arana.direcao,tela)
                    projeteis.append(nova_bala)

        #----------------------COLISOES DO ARANA COM INIMIGOS---------------------------

        rato_colisao = rato.rect.inflate(-45, -15)
        bola1_colisao = bola1.rect.inflate(-50, -35)
        bola2_colisao = bola2.rect.inflate(-50, -35)
        capivara_colisao = capivara.rect.inflate(-60, -70)
        arana_colisao = arana.rect.inflate(-45, -35)

        if tempo_congelado == False:
            if arana_colisao.colliderect(bola1_colisao) or arana_colisao.colliderect(bola2_colisao) or arana_colisao.colliderect(rato_colisao) or arana_colisao.colliderect(capivara_colisao):
                arana.tomar_dano()
                if arana.vivo == False:
                    pygame.mixer.music.load(pathabs4('musica e sons','trilha_sonora_game_over.mp3'))
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(-1)
                    estado = 'game over'
                

        teclas = pygame.key.get_pressed()
        arana.movimento(teclas)


        #--------------------PERSONAGENS E ATAQUES---------------------------------
        arana.atualizar()
        arana.atualizar_animacao()
        arana.desenhar(tela)

        bola1.atualizar_animacao()
        bola2.atualizar_animacao()
        curupira.atualizar_animacao()         #atualiza o frame antes de desenhar
        curupira.draw()                       #desenhar as imagem com o metodo draw

        portal.atualizar_animacao()

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
                    tocar_som(grito_curupira)

            if estado_atual == estado_atacando:
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
                        bola1.rect.x = 1400
                        bola2.rect.x = 1400       
                
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

        elif curupira.vivo == False:
            tempo_congelado = True
            portal.draw()
         
        #----------------------------- outros inimigos ------------------------

        #-----------primeiro rato    ---------------------
        if time_atual - tempo_fase1 > 6000:

            rato.atualizar_animacao()
            rato.draw()
            rato.movimento()   
            
            if rato.rect.x < -190 :   
                rato.direcao = "direita"

            elif rato.rect.x > 1450: 
                rato.direcao = "esquerda"

        #---------------capivara ----------------------  
        if time_atual - tempo_fase1 > 20000:

            capivara.atualizar_animacao()
            capivara.draw()
            capivara.movimento()
             
            if capivara.rect.x < -630 :   
                capivara.direcao = "direita"

            elif capivara.rect.x > 1600: 
                capivara.direcao = "esquerda"

        #---------------------COLISOES DOS PROJETEIS DO ARANA ------------------
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
        game_over = pygame.image.load(pathabs4('imagens', 'fundo', 'game over.png'))
        tela.blit(game_over, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                pygame.mixer.music.load(pathabs4("musica e sons/menu_sound.mp3"))
                pygame.mixer.music.play(-1)
                estado = "menu"


        pygame.display.flip()