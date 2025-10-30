import pygame
from sprite_loader import SpriteSheet

def draw_maze(self, screen, player, ghosts_list):
    screen.fill((0,0,0))
    screen.blit(player.image, player.position)