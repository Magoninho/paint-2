import sys, pygame
from SimpleDrawEngine import *


# gui.main()
pygame.init()
### variáveis

## Cores

white = (255,255,255)
black = (0, 0, 0)

## janela
largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura)) ## janela
pygame.display.set_caption("Isso é uma versão alpha")
screen.fill(white)

running = True ## loop condition

pos = pygame.mouse.get_pos()
last_pos = (0, 0)

## Modos
drawining = False
mode = 0

def draw(mode):
    global pos

    if drawining:
        if mode == 0:
            last_pos = pos
            pos = pygame.mouse.get_pos() # mouse position
            # print(last_pos, pos)
            Line(screen, black, last_pos, pos, 4)
        elif mode == 1:
            last_pos = pos
            pos = pygame.mouse.get_pos() # mouse position
            # print(last_pos, pos)
            Rect(screen, black, (pos, (40, 40)))
        elif mode == 2:
            last_pos = pos
            pos = pygame.mouse.get_pos() # mouse position
            # print(last_pos, pos)
            Circle(screen, black, pos, 50)
    else:
        pos = pygame.mouse.get_pos()
            


## game loop (não coloque muita logica aqui dentro)
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # MODOS PARA MOVIMENTO CONSTANTE DO MOUSE
        elif event.type == pygame.MOUSEMOTION:
            if mode == 0:
                draw(mode)

        # MODOS PARA APENAS UM CLIQUE DO MOUSE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawining = True
            if mode == 1 or mode == 2:
                draw(mode)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            drawining = False
            
        
    pygame.display.update()


