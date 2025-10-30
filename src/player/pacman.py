import pygame

class Pacman:
    def __init__(self, start_pos):
        self.position = start_pos
        self.score = 0

    @staticmethod
    def load_pacman(self, image_pacman):
        pygame.image.load(image_pacman)
        rect = image_pacman.get_rect()

