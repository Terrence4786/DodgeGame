import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge Game")

# Player
player = pygame.Rect(375, 520, 50, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5

    if keys[pygame.K_RIGHT]:
        player.x += 5

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (50, 150, 255), player)

    pygame.display.flip()

pygame.quit()