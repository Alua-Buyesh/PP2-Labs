import pygame
import time
import random
from pygame.locals import *

pygame.init()
score = 0
f_score =0
snake_speed = 5
my_font = pygame.font.SysFont('Verdana', 80)
window_x = 600
window_y = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

wall_rect1 = pygame.Rect(100, 100, 20, 200)
wall_rect2 = pygame.Rect(500, 100, 20, 200)
wall_rect3 = pygame.Rect(100, 500, 200, 20)

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()
FOOD_TIMER1 = 60
FOOD_TIMER2 = 40

snake_position = [300, 300]

snake_body = [[300, 300],[280, 300],[260, 300],[240, 300]]
fruit_position = [random.randrange(1, (window_x//20)) * 20, random.randrange(1, (window_y//20)) * 20]
apple = [random.randrange(1, (window_x//20)) * 20, random.randrange(1, (window_y//20)) * 20]

fruit_spawn = True
apple_spawn = True

direction = 'RIGHT'
change_to = direction

f_score = 0
level = 0

P = True

def S(score):
    return score
def level1():
    global P
    global snake_body
    game_window.fill(black)
    game_over_surface_l = my_font.render('level: ' + str(level), True, white)
    game_window.blit(game_over_surface_l, (180,300))
    P = False
    pygame.display.update()
    time.sleep(2)

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(max(f_score, score)), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def show_level(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Level : ' + str(level), True, color)
    game_window.blit(score_surface, (0, 20))

def game_over(conn, score, level):
    game_window.fill(black)
    game_over_surface = my_font.render('Game Over', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/3)
    game_window.blit(game_over_surface, game_over_rect)

    score_surface = my_font.render('Score: ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_x/2, window_y/2)
    game_window.blit(score_surface, score_rect)

    level_surface = my_font.render('Level: ' + str(level), True, white)
    level_rect = level_surface.get_rect()
    level_rect.midtop = (window_x/2, window_y/1.5)
    game_window.blit(level_surface, level_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()

    # Save score and level to the database
    cur = conn.cursor()
    cur.execute("INSERT INTO scores (score, level) VALUES (%s, %s)", (score, level))
    conn.commit()

# Main game loop
while True:
    if score >= 20:
        P = True
        level += 1
        f_score += score
        score = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 20
    if direction == 'DOWN':
        snake_position[1] += 20
    if direction == 'LEFT':
        snake_position[0] -= 20
    if direction == 'RIGHT':
        snake_position[0] += 20

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 5
        fruit_spawn = False
    if snake_position[0] == apple[0] and snake_position[1] == apple[1]:
        score += 1
        apple_spawn = False
    else:
        snake_body.pop()

    FOOD_TIMER1 -= 1
    if FOOD_TIMER1 == 0:
        game_window.fill(black)
        apple_spawn = False
        FOOD_TIMER1 = 48

    FOOD_TIMER2 -= 1
    if FOOD_TIMER2 == 0:
        game_window.fill(black)
        fruit_spawn = False
        FOOD_TIMER2 = 25

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//20)) * 20, random.randrange(1, (window_y//20)) * 20]

    if not apple_spawn:
        apple = [random.randrange(1, (window_x//20)) * 20, random.randrange(1, (window_y//20)) * 20]

    fruit_spawn = True
    apple_spawn = True
    game_window.fill(black)

    if level == 1:
        if P:
            level1()

        pygame.draw.rect(game_window, white, wall_rect1)
        if snake_position[0] == wall_rect1.x and snake_position[1] >= wall_rect1.y and snake_position[1] <= wall_rect1.y + wall_rect1.height:
            game_over(conn, score, level)

    if level == 2:
        if P:
            level1()

        if snake_position[0] == wall_rect1.x and snake_position[1] >= wall_rect1.y and snake_position[1] <= wall_rect1.y + wall_rect1.height:
            game_over(conn, score, level)
        if snake_position[0] == wall_rect2.x and snake_position[1] >= wall_rect2.y and snake_position[1] <= wall_rect2.y + wall_rect2.height:
            game_over(conn, score, level)
        pygame.draw.rect(game_window, white, wall_rect1)
        pygame.draw.rect(game_window, white, wall_rect2)

    if level == 3:
        if P:
            level1()

        if snake_position[0] == wall_rect1.x and snake_position[1] >= wall_rect1.y and snake_position[1] <= wall_rect1.y + wall_rect1.height:
            game_over(conn, score, level)
        if snake_position[0] == wall_rect2.x and snake_position[1] >= wall_rect2.y and snake_position[1] <= wall_rect2.y + wall_rect2.height:
            game_over(conn, score, level)
        if snake_position[0] == wall_rect3.x and snake_position[1] >= wall_rect3.y and snake_position[1] <= wall_rect3.y + wall_rect3.height:
            game_over(conn, score, level)
        pygame.draw.rect(game_window, white, wall_rect1)
        pygame.draw.rect(game_window, white, wall_rect2)
        pygame.draw.rect(game_window, white, wall_rect3)

    if level == 4:
        level = 3
        game_over(conn, score, level)

    for pos in snake_body:
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(game_window, red, pygame.Rect(apple[0], apple[1], 20, 20))
    pygame.draw.rect(game_window, yellow, pygame.Rect(fruit_position[0], fruit_position[1], 20, 20))

    if snake_position[0] < 0 or snake_position[0] > window_x-20:
        game_over(conn, score, level)
    if snake_position[1] < 0 or snake_position[1] > window_y-20:
        game_over(conn, score, level)

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over(conn, score, level)

    show_score(white, 'Verdana', 20)
    show_level(white, 'Verdana', 20)

    pygame.display.update()
    fps.tick(snake_speed)
