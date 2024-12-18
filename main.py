import pygame
from block import Block
from note import Note
import threading

pygame.init()
screen = pygame.display.set_mode((250, 600))
clock = pygame.time.Clock()
running = True

block = Block(screen.get_width()/2 - 25, screen.get_height()/2 - 25, 50, 50)

channel = pygame.mixer.find_channel()

timings = [
    Note(440, 1, 2),
    Note(440, 1, 2),
    Note(523.25, 0.5, 1)
]

index = 0

left_wall_border = -0.5*((timings[index].total_length*300)-210)

right_wall_border = -0.5*((timings[index].total_length*300)-210)

velocity = [5,5]

my_font = pygame.font.SysFont('arial', 15)

bip = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    block.draw(screen)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, left_wall_border, screen.get_height())) # left wall

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(screen.get_width()-right_wall_border, 0, right_wall_border, screen.get_height())) # right wall

    text_surface = my_font.render(str(clock.get_fps())[:5], False, (255, 0, 0))
    screen.blit(text_surface, (0, 0))
    text_surface = my_font.render(str(left_wall_border), False, (255, 0, 0))
    screen.blit(text_surface, (0, screen.get_height()-text_surface.get_height()))
    text_surface = my_font.render(str(right_wall_border), False, (255, 0, 0))
    screen.blit(text_surface, (screen.get_width()-text_surface.get_width(), screen.get_height()-text_surface.get_height()))

    bip += 1

    if right_wall_border >= block.left or left_wall_border >= block.left:
        threading.Thread(target=timings[index % len(timings)].play, daemon=True).start()
        if right_wall_border < left_wall_border:
            right_wall_border = -((timings[index % len(timings)].total_length * 300) - 100)
            pass
        else:
            left_wall_border = -((timings[index % len(timings)].total_length * 300) - 100)
            pass
        velocity[0] *= -1
        print(bip/60)
        bip = 0
        index += 1

    right_wall_border += velocity[0]
    left_wall_border -= velocity[0]

    pygame.display.flip()

    clock.tick(60)

pygame.quit()