import unittest
from src.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Lager", 4.5)

    def test_drink_has_name(self):
        self.assertEqual("Lager", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(4.5, self.drink.price)