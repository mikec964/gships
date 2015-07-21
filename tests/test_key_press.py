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
    key_state = pygame.key.get_pressed()
    if key_state[K_k]:
        print('k!')
    if key_state[K_ESCAPE]:
        done = True

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    pygame.display.update()
    fps_clock.tick(FPS)

pygame.quit()
sys.exit()
