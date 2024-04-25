import pygame
import psycopg2
import time
import random
from pygame.locals import *

username =""
def connect_to_db():
    try:
        conn = psycopg2.connect(
            database="Tsis10db",
            user="postgres",
            host="localhost",
            password="1234",
            port=5433
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def create_tables(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                username VARCHAR(30),
                user_id INT REFERENCES users(id),
                score INT,
                level INT
            );
        """)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def register_or_get_user(conn):
    try:
        cur = conn.cursor()
        global username
        username = input("Enter your username: ")
        cur.execute("SELECT id, username FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        if user:
            print(f"Welcome back, {username}!")
            return user[0] 
        else:
            cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
            user_id = cur.fetchone()[0]
            conn.commit()
            print(f"Welcome, {username}! You're a new player.")
            return user_id
    except psycopg2.Error as e:
        conn.rollback() 
        print("Error registering user:", e)
        return None

def get_user_level(conn, user_id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
        level = cur.fetchone()
        return level[0] if level else 1  # Default level is 1 if no record found
    except psycopg2.Error as e:
        print("Error getting user level:", e)
        return None

def save_game_state(conn, username, user_id, score):
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO user_score (user_id, username, score) VALUES (%s, %s, %s)",
            (user_id, username, score)
        )
        conn.commit()
        print("Game state saved successfully.")
    except psycopg2.Error as e:
        conn.rollback()  
        print("Error saving game state:", e)


def main():
    global score
    pygame.init() 
    pygame.font.init()  
    conn = connect_to_db()
    if conn:
        create_tables(conn)
        user_id = register_or_get_user(conn)
        if user_id is not None:
            game_state = "Some game state data here..."
            score = 0
            f_score = 0
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

            snake_body = [[300, 300], [280, 300], [260, 300], [240, 300]]
            fruit_position = [random.randrange(1, (window_x // 20)) * 20, random.randrange(1, (window_y // 20)) * 20]
            apple = [random.randrange(1, (window_x // 20)) * 20, random.randrange(1, (window_y // 20)) * 20]

            fruit_spawn = True
            apple_spawn = True

            direction = 'RIGHT'
            change_to = direction

            f_score = 0
            level = 0

            P = True

            def level1():
                global P
                global snake_body
                game_window.fill(black)
                game_over_surface_l = my_font.render('level: ' + str(level), True, white)
                game_window.blit(game_over_surface_l, (180, 300))
                P = False
                pygame.display.flip()
                time.sleep(1)

            def show_score(color, font, size):
                pygame.font.init() 
                score_font = pygame.font.SysFont(font, size)
                score_surface = score_font.render('Score : ' + str(max(f_score, score)), True, color)
                game_window.blit(score_surface, (10, 10))

            def show_level(color, font, size):
                score_font = pygame.font.SysFont(font, size)
                score_surface = score_font.render('Level : ' + str(level), True, color)
                game_window.blit(score_surface, (10, 40)) 

            def game_over(conn, username, score, level):
                game_window.fill(black)
                game_over_surface = my_font.render('Game Over', True, white)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (window_x / 2, window_y / 3)
                game_window.blit(game_over_surface, game_over_rect)

                score_surface = my_font.render('Score: ' + str(score), True, white)
                score_rect = score_surface.get_rect()
                score_rect.midtop = (window_x / 2, window_y / 2)
                game_window.blit(score_surface, score_rect)

                level_surface = my_font.render('Level: ' + str(level), True, white)
                level_rect = level_surface.get_rect()
                level_rect.midtop = (window_x / 2, window_y / 1.5)
                game_window.blit(level_surface, level_rect)
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()

                cur = conn.cursor()
                cur.execute("INSERT INTO user_score (user_id, username, score, level) VALUES (%s,%s, %s, %s)", (user_id,username, score, level))
                conn.commit()

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
                    fruit_position = [random.randrange(1, (window_x // 20)) * 20, random.randrange(1, (window_y // 20)) * 20]

                if not apple_spawn:
                    apple = [random.randrange(1, (window_x // 20)) * 20, random.randrange(1, (window_y // 20)) * 20]

                fruit_spawn = True
                apple_spawn = True
                game_window.fill(black)

                if level == 1:
                    if P:
                        level1()
                    P=False
                    pygame.draw.rect(game_window, white, wall_rect1)
                    if snake_position[0] == wall_rect1.x and wall_rect1.y <= snake_position[1] <= wall_rect1.y + wall_rect1.height:
                        game_over(conn, username, score, level)

                if level == 2:
                    if P:
                        level1()
                    P=False
                    if snake_position[0] == wall_rect1.x and wall_rect1.y <= snake_position[1] <= wall_rect1.y + wall_rect1.height:
                        game_over(conn, username, score, level)
                    if snake_position[0] == wall_rect2.x and wall_rect2.y <= snake_position[1] <= wall_rect2.y + wall_rect2.height:
                        game_over(conn, username, score, level)

                    pygame.draw.rect(game_window, white, wall_rect1)
                    pygame.draw.rect(game_window, white, wall_rect2)

                if level == 3:
                    if P:
                        level1()
                    P=False
                    if snake_position[0] == wall_rect1.x and wall_rect1.y <= snake_position[1] <= wall_rect1.y + wall_rect1.height:
                        game_over(conn, username, score, level)
                    if snake_position[0] == wall_rect2.x and wall_rect2.y <= snake_position[1] <= wall_rect2.y + wall_rect2.height:
                        game_over(conn, username, score, level)
                    if snake_position[0] == wall_rect3.x and wall_rect3.y <= snake_position[1] <= wall_rect3.y + wall_rect3.height:
                        game_over(conn, username, score, level)
                    pygame.draw.rect(game_window, white, wall_rect1)
                    pygame.draw.rect(game_window, white, wall_rect2)
                    pygame.draw.rect(game_window, white, wall_rect3)

                if level == 4:
                    level = 3
                    game_over(conn, username, score, level)

                for pos in snake_body:
                    pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 20, 20))
                pygame.draw.rect(game_window, red, pygame.Rect(apple[0], apple[1], 20, 20))
                pygame.draw.rect(game_window, yellow, pygame.Rect(fruit_position[0], fruit_position[1], 20, 20))

                if snake_position[0] < 0 or snake_position[0] > window_x - 20:
                    game_over(conn, username, score, level)
                if snake_position[1] < 0 or snake_position[1] > window_y - 20:
                    game_over(conn, username, score, level)

                for block in snake_body[1:]:
                    if snake_position[0] == block[0] and snake_position[1] == block[1]:
                        game_over(conn, username, score, level)

                show_score(white, 'Verdana', 20)
                show_level(white, 'Verdana', 20)

                pygame.display.update()
                fps.tick(snake_speed)
        save_game_state(conn, username, user_id, score)


if __name__ == "__main__":
    main()
