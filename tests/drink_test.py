import unittest
from src.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Lager", 4.5)


