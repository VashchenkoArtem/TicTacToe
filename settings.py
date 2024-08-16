import pygame
import modules.path_to_file as path_to_file

class Settings:
    def __init__(self, x = 0, y = 0, name = None, width = 0, height = 0):
        self.X = x
        self.Y = y
        self.NAME = name
        self.IMG = None
        self.WIDTH = width
        self.HEIGHT = height
    
    def load_image(self):
        load_file = pygame.image.load(path_to_file.path_file(self.NAME))
        self.IMG = pygame.transform.scale(load_file, (self.WIDTH, self.HEIGHT))

    def blit_sprite(self, screen):
        screen.blit(self.IMG, (self.X, self.Y))
