'''import pygame 
pygame.init()

X = 400
Y = 400
YELLOW = (240, 255, 15)
NAVY_BLUE = (30, 0, 180)
DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(YELLOW)
    pygame.draw.circle(DISPLAY, NAVY_BLUE, (200, 200), 100)
    pygame.display.flip()'''






'''import pygame 
pygame.init()

X = 400
Y = 400
WHITE = (255, 255, 255)
BLUE = (30, 0, 180)
BLACK = (0, 0, 0)
Orange = (240, 152, 0)
DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLUE)
    pygame.draw.circle(DISPLAY, WHITE, (200, 80), 40)
    pygame.draw.circle(DISPLAY, WHITE, (200, 170), 60)
    pygame.draw.circle(DISPLAY, WHITE, (200, 300), 80)
    pygame.draw.circle(DISPLAY, BLACK, (200, 200), 10)
    pygame.draw.circle(DISPLAY, BLACK, (200, 150), 10)
    pygame.draw.circle(DISPLAY, BLACK, (200, 250), 10)
    pygame.draw.circle(DISPLAY, BLACK, (180, 65), 5)
    pygame.draw.circle(DISPLAY, BLACK, (220, 65), 5)
    pygame.draw.circle(DISPLAY, Orange, (200, 85), 5)
    pygame.display.flip()'''



import pygame 
pygame.init()

X = 400
Y = 400
red = (255,15,15)
WHITE = (255, 255, 255)
NAVY_BLUE = (30, 0, 180)
DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(NAVY_BLUE)
    pygame.draw.circle(DISPLAY, red, (200, 200), 170)
    pygame.draw.circle(DISPLAY, red, (200, 200), 100)
    pygame.draw.circle(DISPLAY, red, (200, 200), 100)
    pygame.draw.circle(DISPLAY, red, (200, 200), 160)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 130)
    pygame.display.flip()