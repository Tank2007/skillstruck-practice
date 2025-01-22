import pygame 
pygame.init()
custom_title = input("Name of title")

x = 400
y = 400
GREEN = (140, 250, 90)
BLUE = (15,251,255)

DISPLAY = pygame.display.set_mode([x,y])
pygame.display.set_caption(custom_title)

#runing of the game 

running = True 

while running:
    
    DISPLAY.fill(GREEN)
    pygame.display.flip()