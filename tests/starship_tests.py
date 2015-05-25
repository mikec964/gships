#!/usr/bin/env python3

import unittest

# These three lines enable you to run this from within your IDE
import os
import sys
sys.path.append(os.path.abspath('..'))

# import starship
import spacewarish.starship as starship

class Starship_tests(unittest.TestCase):
    """ Tests for the starship module"""

    def test_init_ship(self):
        ship1 = starship.Ship('pirate ship0', 100, 200, 90)
        self.assertEqual(ship1.x, 100)
        self.assertEqual(ship1.y, 200)
        self.assertEqual(ship1.heading, 90)
        self.assertEqual(ship1.speed, 0)

    def test_fly_ship(self):
        ship1 = starship.Ship('pirate ship0', 100, 200, 90)
        ship1.accelerate()
        self.assertEqual(ship1.speed, 5)
        ship1.move()
        self.assertEqual(ship1.x, 105)
        self.assertEqual(ship1.y, 200)

if __name__ == '__main__':
    unittest.main()
