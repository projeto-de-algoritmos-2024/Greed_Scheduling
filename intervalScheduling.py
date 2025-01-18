import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Constantes de configuração
offsetX = 30
screen_width = 1100 + (offsetX*2)

screen_height = 900
offsetY = screen_height/2

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Interval Scheduling')

# Definir cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

font = pygame.font.SysFont('arial', 30)

def desenhar_linha():
    start_pos = (offsetX, offsetY)
    end_pos = (screen_width-offsetX, offsetY)
    pygame.draw.line(screen, BRANCO, start_pos, end_pos, 3)

def desenhar_tarefa(tarefa):
    inicio = (tarefa[1] * 100) + offsetX
    termino = ((tarefa[2]-tarefa[1]) * 100) 
    pygame.draw.rect(screen, AZUL, (inicio, offsetY-50, termino, 50))
    pygame.draw.line(screen, VERMELHO, (inicio, offsetY), (inicio, offsetY-50), 3)

    texto = '{}'.format(tarefa[0])  # Formata string 
    text = font.render(texto, True, PRETO, AZUL)
    textRect = text.get_rect()
    textRect.center = (inicio+(termino/2), offsetY-30)
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

tarefas = [('A', 0, 6), ('B', 1, 4), ('C', 3, 5), ('D', 3, 8), ('E', 4, 7), ('F', 5, 9), ('G', 6, 10), ('H', 8, 11)] # Tarefas iguais ao slide

def game_loop():
    running = True

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

        pygame.display.flip()

        
game_loop()