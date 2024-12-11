import pygame
from block import Block
from wall import Wall

pygame.init()
screen = pygame.display.set_mode((250, 600))
clock = pygame.time.Clock()
running = True

block = Block(screen.get_width()/2 - 25, screen.get_height()/2 - 25, 50, 50)

left_wall = Wall(0, 0, 20, screen.get_height(), True)

right_wall = Wall(screen.get_width()-20, 0, 20, screen.get_height(), True)

velocity = [1,1]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    block.draw(screen)

    left_wall.update(velocity, block, screen)
    left_wall.draw(screen)

    right_wall.update(velocity, block, screen)
    right_wall.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()