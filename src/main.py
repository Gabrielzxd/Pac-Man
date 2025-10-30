from sys import exit
import pygame
import json
from .level.sprite_loader import SpriteSheet
from assets.constants import Constants

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
        pygame.display.set_caption(Constants.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.run = True

    def new_game(self):
        self.sprites = pygame.sprite.Group()
        self.runner()

    def runner(self):
        self.playing = True
        while self.playing:
            self.clock.tick(Constants.FPS)
            self.events()
            self.update_sprites()
            self.draw_sprites()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.run = False

    def update_sprites(self):
        self.sprites.update()

    def draw_sprites(self):

