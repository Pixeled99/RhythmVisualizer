import pygame
from base_object import Base
from block import Block

class Wall(Base):
    def __init__(self, left, top, width, height, outer):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.outer = outer

    def update(self, velocity, block : Block, screen):
        if self.left != 0:
            self.left -= velocity[0]
            self.width += velocity[0]
        else:
            self.width -= velocity[0]
        if not self.outer:
            self.top -= velocity[1]
        if self.left == (screen.get_width() - block.width)/2 - self.width or self.left == (screen.get_width() + block.width)/2:
            velocity[0] *= -1

    def draw(self, screen : pygame.Surface):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.left, self.top, self.width, self.height))