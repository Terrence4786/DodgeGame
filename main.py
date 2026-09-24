import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge Game")

# Player
player = pygame.Rect(375, 520, 50, 50)

# Obstacle
obstacle = pygame.Rect(375, 0, 50, 50)
obstacle_speed = 5


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

        # Make the obstacle fall
        obstacle.y += obstacle_speed

        # Reset the obstacle to the top if it goes off the screen
        if obstacle.y > 600:
            obstacle.y = 0
            obstacle.x = random.randint(0, 750)

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (50, 150, 255), player)
    pygame.draw.rect(screen, (255, 50, 50), obstacle)
    pygame.display.flip()

pygame.quit()