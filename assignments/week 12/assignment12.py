#Assignment 12 Rachel Weller
import pygame

pygame.init()
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Abstract Moving Art")

clock = pygame.time.Clock()

mySurface = pygame.Surface((300, 300))
mySurface.fill("azure4")

circle_center = (200, 150)
circle_radius = 40
pygame.draw.circle(mySurface, "aquamarine", circle_center, circle_radius)

pygame.draw.rect(mySurface, "orange", [50,50,100,30], 0, 5)

moving_rect = pygame.Rect(10,10,50,50)
rect_color = "salmon"
speed = [2,2]

circle_rect = pygame.Rect(
    circle_center[0] - circle_radius,
    circle_center[1] - circle_radius,
    circle_radius * 2,
    circle_radius * 2
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    moving_rect.x += speed[0]
    moving_rect.y += speed[1]

    if moving_rect.left < 0 or moving_rect.right > 300:
        speed[0] *= -1
    if moving_rect.top < 0 or moving_rect.bottom > 300:
        speed[1] *= -1

    if moving_rect.colliderect(circle_rect):
        rect_color = "red"
    else:
        rect_color = "salmon"

    mySurface.fill("azure4")
    pygame.draw.circle(mySurface, "aquamarine", circle_center, circle_radius)
    pygame.draw.rect(mySurface, "orange", [50,50, 100, 30], 0, 5)
    pygame.draw.rect(mySurface, rect_color, moving_rect)

    display.fill("white")
    display.blit(mySurface, (100,100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
