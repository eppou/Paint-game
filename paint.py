import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definição de espessuras
THIN = 1
MEDIUM = 3
THICK = 5

# Definição das configurações iniciais
current_color = BLACK
current_thickness = MEDIUM
drawing = False

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desenho com Pygame")

# Função para desenhar na tela
def draw_line(start, end, thickness):
    pygame.draw.line(screen, current_color, start, end, thickness)

# Função para limpar a tela
def clear_screen():
    screen.fill(WHITE)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                drawing = True
            elif event.button == 3:  # Botão direito do mouse
                if current_color == BLACK:
                    current_color = RED
                elif current_color == RED:
                    current_color = GREEN
                else:
                    current_color = BLACK
            elif event.button == 2:  # Botão do meio do mouse
                current_color = WHITE  # Borracha
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Botão esquerdo do mouse
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                draw_line(event.pos, event.pos, current_thickness)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # Tecla D para limpar a tela
                clear_screen()

    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()
sys.exit()
