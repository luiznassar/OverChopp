#é um arquivo para alternar ele e com o menu na main, o jogo começa executando o menu e dps é só executar o rodar jogo
import pygame
from game_content.movimentacao_personagem import player
from constant import SCREEN, WIDTH, HEIGHT, CLOCK, VEL_PLAYER, FPS



def rodar_jogo():
    #inicializa o pygame
    pygame.init()
    #cria o objeto player chamando a classe player e passando as posicoes iniciais do player na tela
    jogador = player(WIDTH // 2, HEIGHT // 2)
    #loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #pega o estado atual do teclado
        keys = pygame.key.get_pressed()
        #verifica se a tecla W, S, A ou D está pressionada e chama a função de movimentação correspondente
        #e verifica colisoes com a borda da tela e posteriormente pode ser implementado colisao com outros objetos
        if keys[pygame.K_w] and jogador.rect.top > 0:
            jogador.movimentacao(0, -1)
        if keys[pygame.K_s] and jogador.rect.bottom < HEIGHT:
            jogador.movimentacao(0, 1)
        if keys[pygame.K_a] and jogador.rect.left > 0:
            jogador.movimentacao(-1, 0)
        if keys[pygame.K_d] and jogador.rect.right < WIDTH : 
            jogador.movimentacao(1, 0)
        #preenche a tela com a cor preta
        SCREEN.fill((0, 0, 0))
        #coloca o jogador na tela
        SCREEN.blit(jogador.imagem, jogador.rect)
        #atualiza a tela
        pygame.display.flip()# Atualiza a tela
        CLOCK.tick(FPS)