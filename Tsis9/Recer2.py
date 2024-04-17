import pygame, random, time
from pygame.locals import *

pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

#Делаю шаблон для шрифторв
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, WHITE)

background = pygame.image.load("Music and png/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("CARS")


#создать персонажей
class Money1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        a = pygame.image.load("Music and png/coin.png")
        self.image = pygame.transform.scale(a, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COINS
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    
            
class Money2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        a = pygame.image.load("Music and png/vecteezy_red-dish-mockup-png-plate_8492307.png")
        self.image = pygame.transform.scale(a, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COINS
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Music and png/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Music and png/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
M1 = Money1()
M2 = Money2()


#добавить их как один единый организм
enemies.add(E1)

coin_group1 = pygame.sprite.Group()
coin_group1.add(M1)
coin_group2 = pygame.sprite.Group()
coin_group2.add(M2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin_group1)
all_sprites.add(coin_group2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 6000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1
        if event.type == QUIT:
            pygame.quit()

    #добавляет в левый угол счетчики
    DISPLAYSURF.blit(background, (0, 0))
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (10, 30))

    #смотрит столкнулись ли они между собой
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        #если игрок и машина столкнется
        if pygame.sprite.spritecollideany(P1, enemies):
            time.sleep(0.8)

            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(game_over, (30, 250))
            DISPLAYSURF.blit(f_score, (100, 500))
            DISPLAYSURF.blit(f_coins, (200, 500))

            pygame.display.update()
            time.sleep(3)
            pygame.quit()
        #если игрок столкнется с монеткой
        if pygame.sprite.spritecollideany(P1, coin_group1):
            collided_coin = pygame.sprite.spritecollideany(P1, coin_group1)
            collided_coin.kill()
            COINS += 1
            pygame.display.update()
            if not any(isinstance(sprite, Money1) for sprite in coin_group1):
                new_coin = Money1() 
                coin_group1.add(new_coin)
                all_sprites.add(new_coin)

        if pygame.sprite.spritecollideany(P1, coin_group2):
            collided_coin = pygame.sprite.spritecollideany(P1, coin_group2)
            collided_coin.kill()
            COINS += 5
            pygame.display.update()
            if not any(isinstance(sprite, Money2) for sprite in coin_group2):
                new_coin = Money2() 
                coin_group2.add(new_coin)
                all_sprites.add(new_coin)

            

    f_coins = font_small.render(f"Coins: {COINS}", True, WHITE)
    f_score = font_small.render(f"Score: {SCORE}", True, WHITE)

    pygame.display.update()
    FramePerSec.tick(FPS)