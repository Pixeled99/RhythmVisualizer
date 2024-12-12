import pygame
from block import Block

pygame.init()
screen = pygame.display.set_mode((250, 600))
clock = pygame.time.Clock()
running = True

block = Block(screen.get_width()/2 - 25, screen.get_height()/2 - 25, 50, 50)

channel = pygame.mixer.find_channel()

bpm = 120

left_wall_border = -0.5*(((60/bpm)*300)-200)

right_wall_border = -0.5*(((60/bpm)*300)-200)

velocity = [5,5]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    block.draw(screen)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, left_wall_border, screen.get_height())) # left wall

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(screen.get_width()-right_wall_border, 0, right_wall_border, screen.get_height())) # right wall


    if right_wall_border >= block.left or left_wall_border >= block.left:
        velocity[0] *= -1
        channel.play(pygame.mixer.Sound("click.mp3"))
        bip = 0

    right_wall_border += velocity[0]
    left_wall_border -= velocity[0]

    pygame.display.flip()

    clock.tick(60)

pygame.quit()