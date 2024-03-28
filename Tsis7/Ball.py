import pygame
import sys

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 30
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 11

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if ball_y - ball_speed >= ball_radius:
            ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        if ball_y + ball_speed <= screen_height - ball_radius:
            ball_y += ball_speed
    if keys[pygame.K_LEFT]:
        if ball_x - ball_speed >= ball_radius:
            ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        if ball_x + ball_speed <= screen_width - ball_radius:
            ball_x += ball_speed

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
