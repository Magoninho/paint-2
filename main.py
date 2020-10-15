import sys, pygame
from SimpleDrawEngine import *

pygame.init()

### variáveis

## Cores

white = (255,255,255)

## janela
largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura)) ## janela
pygame.display.set_caption("Isso é uma versão alpha")


running = True ## loop condition

pos = pygame.mouse.get_pos()
last_pos = (0, 0)
drawining = False


## game loop (não coloque muita logica aqui dentro)
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            if drawining:
                last_pos = pos
                pos = pygame.mouse.get_pos() # mouse position
                # print(last_pos, pos)
                pygame.draw.line(screen, white, last_pos, pos, 4)
            else:
                pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawining = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawining = False
            
        
    pygame.display.update()


