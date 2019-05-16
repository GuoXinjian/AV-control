import pygame
pygame.mixer.init()
pygame.mixer.music.load('1.mp3')
while True:
    if pygame.mixer.music.get_busy()==False:
        pygame.mixer.music.play()