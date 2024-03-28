import pygame
import sys

pygame.init()

window = pygame.display.set_mode((900, 200))
pygame.display.set_caption("Music")

Play=pygame.image.load('Music and png/play-buttton.png').convert_alpha()
Stop = pygame.image.load('Music and png/video-pause-button.png').convert_alpha()
Next = pygame.image.load('Music and png/pause-play.png').convert_alpha()
Last = pygame.image.load('Music and png/music-player.png').convert_alpha()

c_Play=pygame.transform.scale(Play,(100,100))
c_Stop=pygame.transform.scale(Stop,(100,100))
c_Next=pygame.transform.scale(Next,(150,150))
c_Last=pygame.transform.scale(Last,(100,100))



_songs = ['Music and png/Toby_Fox_-_Spider_Dance_64962807.mp3', 'Music and png/Korol_i_SHut_-_Durak_i_molniya_48182429.mp3', 'Music and png/Toby_Fox_-_MEGALOVANIA_64962866.mp3']

for i in _songs:
    pygame.mixer.music.load(i)

Button = pygame.Surface((50, 50))

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.play()

_currently_playing_song = None

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def play_last_song():
    global _songs
    _songs = _songs[-1:] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

play = False
while True:
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if play:
                    pygame.mixer.music.pause()
                    play= False
                else:
                    pygame.mixer.music.unpause()
                    play= True
            if event.key==pygame.K_RIGHT:
                play_next_song()
                play = True
            if event.key==pygame.K_LEFT:
                play_last_song()
                play = True


        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pos[0] < 600 and pos[0] > 300) and (pos[1] < 200 and pos[1] > 50):
                window.fill((255, 255, 255))
                if play:
                    pygame.mixer.music.pause()
                    window.blit(c_Stop, (450,50))
                    pygame.display.update()
                    play= False
                else:
                    pygame.mixer.music.unpause()
                    Button.blit(c_Play, (450, 50))
                    pygame.display.update()
                    play= True

            elif (pos[0] < 900 and pos[0] > 600) and (pos[1] < 200 and pos[1] > 50):
                play_next_song()
                play = True
            elif (pos[0] < 300 and pos[0] > 0) and (pos[1] < 200 and pos[1] > 50):
                play_last_song()
                play = True
        if event.type == SONG_END:
            play_next_song()
    

    window.fill((255, 255, 255))
    window.blit(c_Stop, (400,50))
    window.blit(c_Last, (150, 50))
    window.blit(c_Next, (620, 20))

    pygame.display.flip()