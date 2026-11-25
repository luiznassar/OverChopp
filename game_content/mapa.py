import pygame
import sys
import os

#importando constantes necessárias
from constant import SCREEN, WIDTH, HEIGHT 

# localiza a pasta atual, e vai para a de imagens para carregar a imagem do mapa
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_IMAGEM = os.path.join(PASTA_ATUAL, "..", "imagens", "mapa_bar.png")

# carrega a imagem e ajusta para o tamanho da tela
IMAGEM_MAPA = pygame.image.load(CAMINHO_IMAGEM)
IMAGEM_MAPA = pygame.transform.scale(IMAGEM_MAPA, (WIDTH, HEIGHT))

#definindo a grade
TAMANHO_TILE = 48
COLUNAS = 27
LINHAS = 16
OFFSET_X = (WIDTH - (COLUNAS * TAMANHO_TILE)) // 2
OFFSET_Y = 0

#matriz invisível para colisão
MATRIZ_MAPA = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
    [1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1], 
    [1,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1], 
    [1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1], 
    [1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1], 
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], 
    [1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1], 
    [1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1], 
    [1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], 
    [1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1], 
    [1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1], 
    [1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1], 
    [1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1], 
    [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1], 
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
]





