#Cat moving horizontally, pink background:
import pygame

# constants
screen_width = 1200
screen_height = 300
background_color = (255, 192, 203)

# activate pygame
pygame.init()

# creates screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('cat image')

# load image
img = pygame.image.load("cat.png").convert_alpha()

# scale image
img = pygame.transform.scale(img, (100, 100))

cat_x = 100
cat_y = 100

# init clock
clock = pygame.time.Clock()

# main loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cat_x < screen_width:
        cat_x += 3
    else:
        cat_x = 0

    # fill background
    screen.fill(background_color)

    screen.blit(img, (cat_x, cat_y))

    # update display
    pygame.display.flip()

pygame.quit()
