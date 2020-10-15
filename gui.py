import pygame, sys

def main():
    pygame.init()
    background = (0, 0, 0)

    ## game loop (não coloque muita logica aqui dentro)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            
        pygame.display.update()


main()