from sys import exit

import pygame
from pygame.locals import *

from level.sprite_loader import *
from level.tiles_tileset import *
from level.logic_map import *

TILE_WIDTH = 8
TILE_HEIGHT = 8
GRID_SPACING = 1
SCALE = 3
FPS = 60

MAP_WIDTH_IN_TILES = len(logic_map[0])
MAP_HEIGHT_IN_TILES = len(logic_map)

SCREEN_WIDTH = MAP_WIDTH_IN_TILES * TILE_WIDTH * SCALE
SCREEN_HEIGHT = MAP_HEIGHT_IN_TILES * TILE_HEIGHT * SCALE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pac-Man')
clock = pygame.time.Clock()

tileset_loader_map = SpriteSheet("assets/graphics/tileset.png", TILE_WIDTH, TILE_HEIGHT, GRID_SPACING)

tile_catalog = []
NUM_TILE_ROWS = 3
NUM_TILE_COLS = 16
for y in range(NUM_TILE_ROWS):
    for x in range(NUM_TILE_COLS):
        tile_catalog.append(tileset_loader_map.get_sprite(x, y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((25,25,25))
    for y, line in enumerate(logic_map):
        for x, tile_id in enumerate(line):
            tile_image = tile_catalog[tile_id]
            scaled_image = pygame.transform.scale(tile_image, (TILE_WIDTH * SCALE, TILE_HEIGHT * SCALE))
            pos_x = x * TILE_WIDTH * SCALE
            pos_y = y * TILE_HEIGHT * SCALE
            screen.blit(scaled_image, (pos_x, pos_y))

    pygame.display.update()

    clock.tick(FPS)