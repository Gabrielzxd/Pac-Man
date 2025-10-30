import pygame

class SpriteSheet:
    def __init__(self, image, tile_size, spacing=0):
        self.sheet = pygame.image.load(image).convert_alpha()
        self.tile_size = tile_size
        self.spacing = spacing

    def get_tile(self, x, y):
        rect = pygame.Rect(
            x * (self.tile_size + self.spacing),
            y * (self.tile_size + self.spacing),
            self.tile_size,
            self.tile_size
        )
        tile = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)
        tile.blit(self.sheet, (0, 0), rect)
        return tile
