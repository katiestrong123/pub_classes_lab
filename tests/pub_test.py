import unittest
from src.pub import *
from src.drink import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Lager", 4.5)
        self.drink_2 = Drink("Rum and Coke", 5.0)
        
        drinks_menu = [self.drink_1, self.drink_2]
        self.pub = Pub("Spicey Dice", 1000, drinks_menu)

    def test_pub_has_name(self):
        self.assertEqual("Spicey Dice",self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(2, self.pub.stock_count())