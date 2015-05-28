#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *
import starship


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


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

    while True:  # game loop
        screen.fill(WHITE)

        #PROCESSES
        checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP:
                print(event.key)
                if event.key in (K_ESCAPE):
                    terminate()
                if event.key in (K_k):
                    pirate.accelerate()
                if event.key in (K_j):
                    pirate.rotate_left(5)
                if event.key in (K_l):
                    pirate.rotate_right(5)

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
