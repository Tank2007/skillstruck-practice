import pygame 
pygame.init()
custom_title = input("Name of title")

x = 400
y = 400
WHITE = (255,255,255)
BLACK = (0, 0, 0)
DISPLAY = pygame.display.set_mode([x,y])
pygame.display.set_caption(custom_title)

#runing of the game 

running = True 

while running:
    
    DISPLAY.fill(WHITE)
    DISPLAY.fill(BLACK)
    pygame.display.flip()