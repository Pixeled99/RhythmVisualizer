import pygame
import threading
from block import Block
from note import Note
from convert import convert

timings = convert("test.mid", 1)

for index, note in enumerate(timings):
    note.total_length = timings[(index+1)%len(timings)].end

pygame.init()
screen = pygame.display.set_mode((250, 600))
clock = pygame.time.Clock()
running = True

block = Block(screen.get_width()/2 - 25, screen.get_height()/2 - 25, 50, 50)

channel = pygame.mixer.find_channel()

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

    bip += 1

    if right_wall_border >= block.left or left_wall_border >= block.left:
        offset = 0
        while timings[index + offset].start == timings[index].start:
            threading.Thread(target=timings[index+offset].play, daemon=True).start()
            offset+=1
        if right_wall_border < left_wall_border:
            right_wall_border = -(((timings[index+offset].start-timings[index].start) * 300) - 100)
            pass
        else:
            left_wall_border = -(((timings[index+offset].start-timings[index].start) * 300) - 100)
            pass
        velocity[0] *= -1
        index += offset

    right_wall_border += velocity[0]
    left_wall_border -= velocity[0]

    pygame.display.flip()

    clock.tick(60)

pygame.quit()