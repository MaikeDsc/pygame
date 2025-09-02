import pygame

pygame.init()

largura = 700
altura = int(largura * 0.8)    # o valor da altura é ajustavel a largura 
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('teste shooter')

#taxas de quadro (frame rate)
relogio = pygame.time.Clock()
fps = 60

#definindo as variaveis de movimento do player 
mover_esquerda = False
mover_direita = False

#definindo uma cor para o backgrownd
bg = (31, 31, 51)

#--------------------------------------------------------------------------------

#função para desenhar o fundo
def desenhar_bg():
    tela.fill(bg)

class Soldado(pygame.sprite.Sprite):
    def __init__(self, nome_pasta, x, y, escala, speed):        #speed define a velocidade para cada intancia dessa classe por pixel a cada loop
        pygame.sprite.Sprite.__init__(self)
        self.nome_pasta = nome_pasta
        self.speed = speed 
        self.direcao = 1
        self.giro = False 
        self.atualizar_time = pygame.time.get_ticks()       # pega o horario atual,em q foi criado a instancia, essencial para trabalhar com as animações
        self.lista_animacoes = []
        self.indice_frame = 0
        self.acao = 0
        lista_temporaria = []
        for c in range(8):
            imagem = pygame.image.load(f'shooter maike/imagens/soldados/{self.nome_pasta}/padrao/{c}.png')
            imagem = pygame.transform.scale(imagem, (int(imagem.get_width() * escala), int(imagem.get_height() * escala)) )
            lista_temporaria.append(imagem)
        self.lista_animacoes.append(lista_temporaria)

        lista_temporaria = []
        for c in range(3):
            imagem = pygame.image.load(f'shooter maike/imagens/soldados/{self.nome_pasta}/corrida/{c}.png')
            imagem = pygame.transform.scale(imagem, (int(imagem.get_width() * escala), int(imagem.get_height() * escala)) )
            lista_temporaria.append(imagem)
        self.lista_animacoes.append(lista_temporaria)
        
        self.img = self.lista_animacoes[self.acao][self.indice_frame]                 #primeira imagem carregada, ou seja o presonagem começa com a imagem padrão
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def movimento(self, mover_esquerda, mover_direita):
        #resetar variaveis de movimento
        dx = 0
        dy = 0

        #atribuir variaveis de movimento e se mover
        if mover_esquerda:
            dx = -self.speed
            self.giro = True
            self.direcao = -1
        if mover_direita:
            dx = self.speed
            self.giro = False
            self.direcao = 1

        #atualizar posição do retangulo, que é onde está a imagem 
        self.rect.x += dx
        self.rect.y += dy

    def atualizar_animacao(self):
        #atualizando animação
        INTERVALO_ANIMACAO = 110                         # é o cooldown de uma animaçaõ para outra, é uma constante
        #atualizando o frame independente da frame tual 
        self.img = self.lista_animacoes[self.acao][self.indice_frame]

        #vendo o horario atual novamente para saber quanto tempo passou desde a ultima checagem
        if pygame.time.get_ticks() - self.atualizar_time > INTERVALO_ANIMACAO:              #se o tempo for maior, passar para o rpoximo quadro
            self.atualizar_time = pygame.time.get_ticks()
            self.indice_frame += 1

        #se as animações acabaram, entao renicie do começo 
        if self.indice_frame >= len(self.lista_animacoes[self.acao]):
            self.indice_frame = 0


    def atualizar_acoes(self, nova_acao):
        #checar se a vova ação é diferente da anterior
        if nova_acao != self.acao:
            self.acao = nova_acao                                         #uma nova ação vai ser definida 
            self.indice_frame = 0                                           #atualiza para o primeiro frame de volta, para ficar mais fluido
            self.atualizar_time = pygame.time.get_ticks()                   #atualiza o relogio de transição de frames tbm

    def draw(self):
        tela.blit(pygame.transform.flip(self.img, self.giro, False) ,self.rect)

#--------------------------------------------------------------------------------

#define a instancia player 
player = Soldado('jogador', 200, 400, 1.5, 5)

inimigo = Soldado('inimigo2', 500, 400, 2, 5)



loop = True
while loop:

    relogio.tick(fps)

    desenhar_bg()                       #backgrownd
    
    player.atualizar_animacao()         #atualiza o frame antes de desenhar
   
    player.draw()                       #desenhar as imagem com o metodo draw

    inimigo.draw()
    
    
    
    #atualizar a ação do jogador 
    if mover_esquerda or mover_direita:
        player.atualizar_acoes(1)           #1 corresponde ao local onde esta a minha lista de correr na lista de animações 
    else:
        player.atualizar_acoes(0)           #0 corresponde ao local de onnde esta a minha lista de animações do personagem obsoleto
   
    player.movimento(mover_esquerda, mover_direita)

    for event in pygame.event.get():
        #sair do jogo
        if event.type == pygame.QUIT: 
            loop = False

        #tecla pessionada se pfoi pressionado alguma tecla do teclado
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_a:                     #se evento da tecla == pressionado_a
                mover_esquerda = True 
            if event.key == pygame.K_d:                     #se evento de tecla  == pressionado_d
                mover_direita = True              
            #para sair com o esc 
            if event.key == pygame.K_ESCAPE:
                loop = False



        #teclas não pressionadas, teclas que foram soltas 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_esquerda = False
            if event.key == pygame.K_d:
                mover_direita = False
    


    pygame.display.update()
pygame.quit()