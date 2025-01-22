import pygame 
pygame.init()

x = 500
y = 500
Blue = (90, 90,250)
White = (255, 255, 255)
Black = (0, 0, 0)

DISPLAY = pygame.display.set_mode([x, y])
running = True

while running:

    DISPLAY.fill(Blue)
    pygame.draw.rect(DISPLAY, White, [150, 150, 100, 20])
    pygame.display.flip()