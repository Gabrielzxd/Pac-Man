import pygame

class SpriteSheet:
    def __init__(self, filename, tile_width, tile_height, grid_spacing):
        try:
            self.sheet = pygame.image.load(filename).convert()
            self.tile_width = tile_width
            self.tile_height = tile_height
            self.grid_spacing = grid_spacing
        except pygame.error:
            raise SystemExit(pygame.error)

    def get_sprite(self, tile_x_index, tile_y_index):
        pixel_x = tile_x_index * (self.tile_width + self.grid_spacing)
        pixel_y = tile_y_index * (self.tile_height + self.grid_spacing)
        tile_rect = pygame.Rect(pixel_x, pixel_y, self.tile_width, self.tile_height)
        tile_image = self.sheet.subsurface(tile_rect)
        tile_surface = tile_image.copy()
        tile_surface.set_colorkey((0, 0, 0))
        return tile_surface