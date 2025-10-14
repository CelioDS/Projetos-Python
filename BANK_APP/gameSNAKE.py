## PARTE 1 DEFINIÇÕES DE VARIAVEIS GLOBAIS

import pygame
import random

#Iniciar jogo
pygame.init()

pygame.display.set_caption("Jogo da Cobrinha")

# Configurações da tela
LARGURA_TELA = 600
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
RELOGIO = pygame.time.Clock()  #

# Parâmetros da cobrinha
TAMANHO_QUADRADO = 20  #Este valor define o tamanho das células que compõem a cobrinha na tela. Cada segmento da cobrinha será desenhado como um quadrado com 20 pixels de lado. Este tamanho ajuda a garantir que a cobrinha seja visível e fácil de seguir durante o jogo.
VELOCIDADE_JOGO = 15   #Este valor determina a velocidade do jogo. Especificamente, ele controla a frequência com que a cobrinha se move na tela. O número 15 define a quantidade de pixels que a cobrinha avança a cada atualização do loop do jogo, resultando na velocidade com que a cobrinha se move.

#Definindo cores que utilizarei no meu jogo
COR_PRETA = (0, 0, 0)
COR_BRANCA = (255, 255, 255)
COR_VERDE = (0, 255, 0)

## PARTE 2 - DEFINIÇÃO DAS FUNÇÕES

def gerar_comida():
    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_QUADRADO) / float(TAMANHO_QUADRADO)) * float(TAMANHO_QUADRADO)
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_QUADRADO) / float(TAMANHO_QUADRADO)) * float(TAMANHO_QUADRADO)
    return comida_x, comida_y
#Desenhar a comida
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(TELA, COR_VERDE,[comida_x,comida_y,tamanho,tamanho])

#Desenhar a cobra
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(TELA, COR_BRANCA, [pixel[0], pixel[1], tamanho, tamanho])

#Controle de Direção

def selecionar_alteracao(tecla):
    if tecla == pygame.K_UP:
        x_alteracao = 0
        y_alteracao = -TAMANHO_QUADRADO
    elif tecla == pygame.K_DOWN:
        x_alteracao = 0
        y_alteracao = TAMANHO_QUADRADO
    elif tecla == pygame.K_LEFT:
        x_alteracao = -TAMANHO_QUADRADO
        y_alteracao = 0
    elif tecla == pygame.K_RIGHT:
        x_alteracao = TAMANHO_QUADRADO
        y_alteracao = 0
    return x_alteracao, y_alteracao


## PARTE 3 - CÓDIGO PRINCIPAL, QUE IRÁ UTILIZAR AS VARIAVEIS E FUNÇÕES DESINIDAS ANTERIORMENTE

def jogar():
    jogo_ativo = True
    contador = 0
    x_cabeca = LARGURA_TELA / 2
    y_cabeca = ALTURA_TELA / 2
    x_alteracao = 0
    y_alteracao = 0
    comprimento_cobra = 1
    pixels_cobra = []
    comida_x, comida_y = gerar_comida()

    while jogo_ativo:
        #Definir a cor da tela
        TELA.fill(COR_PRETA)

        #Verificando se o usuário está interagindo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
            elif evento.type == pygame.KEYDOWN:
                x_alteracao, y_alteracao = selecionar_alteracao(evento.key)

        # Desenhar comida
        desenhar_comida(TAMANHO_QUADRADO, comida_x, comida_y)

        # Atualizar a posição da cobrinha
        if x_cabeca < 0 or x_cabeca >= LARGURA_TELA or y_cabeca < 0 or y_cabeca >= ALTURA_TELA:
            jogo_ativo = False
        x_cabeca += x_alteracao
        y_cabeca += y_alteracao

        # Desenhar cobrinha
        pixels_cobra.append([x_cabeca, y_cabeca])
        if len(pixels_cobra) > comprimento_cobra:
            del pixels_cobra[0]

        # Verificar colisão com o próprio corpo
        for pixel in pixels_cobra[:-1]:
            if pixel == [x_cabeca, y_cabeca]:
                jogo_ativo = False

        desenhar_cobra(TAMANHO_QUADRADO, pixels_cobra)

        # Atualizar a tela
        pygame.display.update()

        # Criar nova comida se necessário
        if x_cabeca == comida_x and y_cabeca == comida_y:
            comprimento_cobra += 1
            comida_x, comida_y = gerar_comida()

        RELOGIO.tick(VELOCIDADE_JOGO)

jogar()
