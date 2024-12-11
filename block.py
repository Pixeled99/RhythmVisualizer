import pygame
from base_object import Base

class Block(Base):
    def draw(self, screen : pygame.Surface):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.left, self.top, self.width, self.height), 5)