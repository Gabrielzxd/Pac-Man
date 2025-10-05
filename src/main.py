import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width, height = 640, 480
x = width / 2   
y = height / 2
FPS = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pac-Man')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))
    pygame.display.update()