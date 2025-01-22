import pygame
import sys

def calculate_age(year_of_birth, current_year):
    difference = current_year - year_of_birth

    if difference > 0:
        return f"You are {difference} year{'s' if difference != 1 else ''} old."
    elif difference < 0:
        return f"You will be born in {-difference} year{'s' if difference != -1 else ''}."
    else:
        return "You were born this very year!"

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Age Calculator")

background_color = (255, , 30)
text_color = (255, 255, 255)
input_color = (50, 50, 50)
input_active_color = (100, 100, 100)

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

input_active = [False, False]  
input_boxes = [pygame.Rect(200, 100, 200, 40), pygame.Rect(200, 160, 200, 40)]
inputs = ["", ""]
result = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, box in enumerate(input_boxes):
                if box.collidepoint(event.pos):
                    input_active[i] = True
                else:
                    input_active[i] = False

        if event.type == pygame.KEYDOWN:
            for i in range(2):
                if input_active[i]:
                    if event.key == pygame.K_BACKSPACE:
                        inputs[i] = inputs[i][:-1]  
                    elif event.key == pygame.K_RETURN and i == 1:
                        
                        try:
                            year_of_birth = int(inputs[0])
                            current_year = int(inputs[1])
                            result = calculate_age(year_of_birth, current_year)
                        except ValueError:
                            result = "Please enter valid numbers."
                    else:
                        inputs[i] += event.unicode  

    screen.fill(background_color)

    for i, box in enumerate(input_boxes):
        color = input_active_color if input_active[i] else input_color
        pygame.draw.rect(screen, color, box)
        text_surface = font.render(inputs[i], True, text_color)
        screen.blit(text_surface, (box.x + 10, box.y + 5))

    screen.blit(small_font.render("Year of Birth:", True, text_color), (50, 110))
    screen.blit(small_font.render("Current Year:", True, text_color), (50, 170))

    result_surface = font.render(result, True, text_color)
    screen.blit(result_surface, (50, 300))

    pygame.display.flip()

pygame.quit()
