import pygame

class Block:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(left, top, width, height)

    def draw(self, screen : pygame.Surface):
        pygame.draw.rect(screen, (0,0,0), self.rect, 5)