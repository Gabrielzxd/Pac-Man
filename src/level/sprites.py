import pygame

class SpriteSheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            raise SystemExit(pygame.error)

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey((0, 0, 0))
        return sprite