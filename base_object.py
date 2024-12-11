import pygame

class Base:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def draw(self, screen : pygame.Surface):
        pass