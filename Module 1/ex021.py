print('======= Exercício aula 08 =======')
print('======= REPRODUZIR MP3 =======')
import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass