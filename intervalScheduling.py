import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Constantes de configuração
offsetX = 30
screen_width = 1100 + (offsetX*2)

screen_height = 900
offsetY = screen_height/2 + 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Interval Scheduling')

# Definir cores
""" PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0) """

COR_FUNDO = (255, 255, 255)
COR_FONTE = (0, 0, 0)
COR_TEXTO_FUNDO = (255, 255, 255)
COR_TAREFA = (0, 0, 255)
COR_SEPARADOR = (255, 0, 0)
COR_LINHA = (0, 0, 0)

font = pygame.font.SysFont('arial', 30)

def desenhar_linha():
    start_pos = (offsetX, offsetY)
    end_pos = (screen_width-offsetX, offsetY)
    pygame.draw.line(screen, COR_LINHA, start_pos, end_pos, 3)

def desenhar_tarefa(tarefa):
    inicio = (tarefa[1] * 100) + offsetX
    termino = ((tarefa[2]-tarefa[1]) * 100) 
    pygame.draw.rect(screen, COR_TAREFA, (inicio, offsetY-50, termino, 50))
    pygame.draw.line(screen, COR_SEPARADOR, (inicio, offsetY), (inicio, offsetY-50), 3)

    texto = '{}'.format(tarefa[0])  # Formata string 
    text = font.render(texto, True, COR_FONTE, COR_TAREFA)
    textRect = text.get_rect()
    textRect.center = (inicio+(termino/2), offsetY-25)
    screen.blit(text, textRect)

def intervalScheduling(tarefas):
    tarefas.sort(key=lambda x: x[2])
    contador = 0
    final = 0
    solucao = []

    for intervalo in tarefas:
        if(final <= intervalo[1]):
            final = intervalo[2]
            contador +=1
            solucao.append(intervalo)
            desenhar_tarefa(intervalo)
    
    print("Maximo de tarefas : ", contador) 
    print("Lista de tarefas : ", solucao) 

def gerar_tarefas():
    tarefas = []
    contador = random.randint(8, 20)
    tempo_max = 11

    for i in range(ord('A'), ord('A') + contador):
        #print(chr(i))
        inicio = random.randint(0, tempo_max - 1)
        fim = random.randint(inicio + 1, tempo_max)
        tarefas.append((chr(i), inicio, fim))
    #print(tarefas)

    return tarefas

def desenhar_lista(tarefas):
    font = pygame.font.SysFont('arial', 15)
    texto = ' LISTA DE TAREFAS: '
    text = font.render(texto, True, COR_FONTE, COR_TEXTO_FUNDO)
    textRect = text.get_rect()
    textRect.left = offsetX
    textRect.top = 10
    screen.blit(text, textRect)

    texto = ' Aperte \'G\' para gerar novas tarefas '
    text = font.render(texto, True, COR_FONTE, COR_TEXTO_FUNDO)
    textRect.left = offsetX + 300
    screen.blit(text, textRect)

    texto = ' Aperte \'I\' para fazer o Interval Scheduling '
    text = font.render(texto, True, COR_FONTE, COR_TEXTO_FUNDO)
    textRect.left = offsetX + 600
    screen.blit(text, textRect)

    texto = ' Aperte \'Esc\' para sair '
    text = font.render(texto, True, COR_FONTE, COR_TEXTO_FUNDO)
    textRect.right = screen_width - offsetX
    screen.blit(text, textRect)

    y = 35
    for tarefa in tarefas:
        texto = ' Tarefa: {} -> Inicio: {} | Fim: {} '.format(tarefa[0], tarefa[1], tarefa[2])  # Formata string 
        font = pygame.font.SysFont('arial', 12)
        text = font.render(texto, True, COR_FONTE, COR_TEXTO_FUNDO)
        textRect = text.get_rect()
        textRect.left = offsetX
        textRect.top = y 
        screen.blit(text, textRect)
        y += 20

def game_loop():
    running = True
    tarefas = [('A', 0, 6), ('B', 1, 4), ('C', 3, 5), ('D', 3, 8), ('E', 4, 7), ('F', 5, 9), ('G', 6, 10), ('H', 8, 11)] # Tarefas iniciais iguais ao slide
    screen.fill(COR_FUNDO)
    desenhar_lista(tarefas)

    while running:
        
        desenhar_linha()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Apertou Esc
                    pygame.quit() #Fecha jogo e programa
                    sys.exit()
                elif event.key == pygame.K_i: # Apertou i
                    intervalScheduling(tarefas)
                elif event.key == pygame.K_g: # Apertou g
                    tarefas = gerar_tarefas()
                    screen.fill(COR_FUNDO)
                    desenhar_lista(tarefas)

        pygame.display.flip()


game_loop()