import pygame
img = pygame.image.load("curse.png")

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame .display.set_mode((screen_width, screen_height))
screen.blit( img,  (0,0))
pygame.display.set_caption("Hotel_Dreamer")
delay = 1
while True:
    pygame.display.update()