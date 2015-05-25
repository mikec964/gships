#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *
import starship


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

    while True:
        screen.fill(WHITE)

        #PROCESSES
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYUP:
                # check if the user pressed a key to slide a tile
                if event.key in (K_UP, K_i):
                    pirate.accelerate()

        #LOGIC
        pirate.move()
        # if pirate.speed > 1:
        #     pirate.speed -= 1       # all ships have drag!
        # else:
        #     pirate.speed = 0

        #DRAW
        screen.blit(pirate.image, (pirate.x, pirate.y))

        #DRAW
        pygame.display.update()
        fps_clock.tick(FPS)

if __name__ == '__main__':
    main()
