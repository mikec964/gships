#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *
import starship


def terminate():
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Space War')

    FPS = 30
    fps_clock = pygame.time.Clock()     # clock is object, Clock is class

    pirate = starship.Ship('pirate ship0', 100, 100, 90)

    orig_keys = pygame.key.get_pressed()
    print(orig_keys)

    while True:  # game loop
        screen.fill(WHITE)

        #PROCESSES
        key_state = pygame.key.get_pressed()
        if orig_keys != key_state:
            print(key_state)
        if key_state[K_k]:
            pirate.accelerate()
            print('accelerate. ')
        elif key_state[K_j]:
            pirate_rotate_left(5)
            print('left. ')
        elif key_state[K_l]:
            pirate_rotate_right(5)
            print('right. ')

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        pygame.event.pump()

        #LOGIC
        # pirate.move()

        #DRAW
        # screen.blit(pirate.image, (pirate.x, pirate.y))

        #DRAW
        pygame.display.update()
        fps_clock.tick(FPS)

if __name__ == '__main__':
    main()
