import pygame
import time
import random
from pygame.locals import *

pygame.init()

snake_speed = 5

window_x = 600
window_y = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = pygame.Color(255, 0, 0)


pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [300,300]

snake_body = [[300, 300],[280, 300],[260, 300],[240, 300]]
fruit_position = [random.randrange(1, (window_x//20)) * 20, random.randrange(1, (window_y//20)) * 20]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score : ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)

def game_over():

	my_font = pygame.font.SysFont('Verdana', 80)
	game_window.fill(black)
	game_over_surface = my_font.render(
		'Score: ' + str(score), True, white)
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (window_x/2, window_y/2)
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	time.sleep(2)
	pygame.quit()
	quit()

while True:
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
	if snake_position[0] == fruit_position[0] and snake_position[1]==fruit_position[1]:
		score += 1
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//20)) * 20, random.randrange(1, (window_y//20)) * 20]
		
	fruit_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, white,
						pygame.Rect(pos[0], pos[1], 20, 20))
	pygame.draw.rect(game_window, red, pygame.Rect(
		fruit_position[0], fruit_position[1], 20, 20))

	if snake_position[0] < 0 or snake_position[0] > window_x-20:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-20:
		game_over()

	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	show_score(1, white, 'Verdana', 20)

	pygame.display.update()

	fps.tick(snake_speed)
