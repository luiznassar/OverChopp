import pygame
from constant import VEL_PLAYER, WIDTH, HEIGHT, SCREEN

class player():
    #funcao que define o respectivo objeto "player"
    def __init__(self, x, y):
        #velocidade do player
        self.vel = VEL_PLAYER
        #define as dimensoes do player(quadrado)
        self.imagem = pygame.Surface((50, 50))
        #torna o player vermelho
        self.imagem.fill((255, 0, 0))
        #imagem player
        self.rect = self.imagem.get_rect()
        #posicoes do quadrado(player) na tela
        self.rect.x = x
        self.rect.y = y

    def movimentacao(self, dx, dy):
        #atualiza essas posicoes do player de acordo com a velocidade e a direcao
        self.rect.x += dx * self.vel
        self.rect.y += dy * self.vel

    

        
