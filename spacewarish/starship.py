import os
import sys
import pygame
from pygame.locals import *


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
