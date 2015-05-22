#!/usr/bin/env python

import pygame
from pygame.locals import *
import os, sys


class Ship(object):
    """A ship has a location and heading"""

    def __init__(self, base_image, start_x, start_y, start_heading):
        # read ../images/players.csv
        datadir = 'images'
        filename = base_image + '.jpg'
        # Use dirname(__file__) so this runs even when called from ../tests
        filepath = os.path.join(os.path.dirname(__file__), os.pardir, datadir, filename)

        try:
            self.image = pygame.image.load(filepath)
        except:
            pygame.quit()
            sys.exit()
            raise

        self.x = start_x
        self.y = start_y
        self.heading = start_heading    # 0 is up, 90 is right, 180 is down
        self.speed = 0

    def accelerate(self):
        MAX_SPEED = 25
        THRUST = 5
        if self.speed <= MAX_SPEED:
            self.speed = self.speed + THRUST
            # print("gun it")

    def move(self):
        self.x = self.x + self.speed
        # print(self.x, self.y, self.heading, self.speed)

def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
    pygame.display.set_caption('Space War')

    FPS = 30
    fps_clock = pygame.time.Clock()     #clock is object, Clock is class

    pirate = Ship('pirate ship0', 100, 100, 90)

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

