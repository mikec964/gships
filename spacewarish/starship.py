import os
import sys
import pygame
from pygame.locals import *


class Ship(object):
    """A ship has a location and heading"""

    def __init__(self, base_image, start_x, start_y, start_heading):
        # read ../images/[shipname].jpg
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

        # Define ship characteristics
        self.MAX_SPEED = 25  # In pixels per second
        self.THRUST = 5  # Max acceleration
        self.MANEUVER = 72  # Max rotation in degrees
        self.TUBES = 4  # Max torps to fire in a salvo

        # Define ship current attributes
        self.x = start_x
        self.y = start_y
        self.heading = start_heading  # 0 is up, 90 is right, 180 is down
        self.speed = 0  # In pixels per second
        self.spinrate = 0  # In degrees per second clockwise

    def accelerate(self):
        if self.speed <= self.MAX_SPEED:
            self.speed = self.speed + self.THRUST
            if self.speed > self.MAX_SPEED:
                self.speed = self.MAX_SPEED

    def spin(self, thrust):
        self.spinrate = thrust
        self.heading = self.heading + self.spinrate
        if self.heading >= 360:
            self.heading = self.heading - 360
        if self.heading < 0:
            self.heading = self.heading + 360

    def rotate_right(self, degrees):
        self.spin(degrees)

    def rotate_left(self, degrees):
        self.spin(-degrees)

    def move(self):
        self.x = self.x + self.speed
        # print(self.x, self.y, self.heading, self.speed)
