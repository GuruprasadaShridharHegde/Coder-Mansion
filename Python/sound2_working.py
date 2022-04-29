import pygame

pygame.mixer.init()
pygame.mixer.music.load("01.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	pass