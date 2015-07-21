import sys
import pygame
from pygame.locals import *

pygame.init()
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
FPS = 30
fps_clock = pygame.time.Clock()     # clock is object, Clock is class

done = False

while not done:
    for event in pygame.event.get():
        # any other key event input
        if event.type == QUIT:
            done = True
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_a:
                print ("Pressed A")

    pygame.display.update()
    fps_clock.tick(FPS)

pygame.quit()
sys.exit()
