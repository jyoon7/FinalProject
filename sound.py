import pygame
file = 'Example.ogg'

# pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Example.ogg")
pygame.mixer.music.play()
pygame.mixer.music.stop()