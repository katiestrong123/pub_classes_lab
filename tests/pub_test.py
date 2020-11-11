import unittest
from src.pub import *
from src.drink import *
from src.customer import *

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
        self.assertEqual(2, self.pub.drinks_list())

    def test_can_increase_till(self):
        # Arrange
        # Act 
        self.pub.increase_till(5.0)
        # Assert 
        self.assertEqual(1005.0, self.pub.till)

    def test_can_find_drink_by_name(self):
        # arrange
        # act
        found_drink = self.pub.find_drink_by_name("Lager")
        # assert
        self.assertEqual(self.drink_1, found_drink)

    def test_can_sell_drink_to_customer(self):
        # Arrange 
        customer = Customer("Ben Benson", 100.0, 33)
        # act
        self.pub.sell_drink_to_customer("Lager", customer)
        # Assert
        self.assertEqual(95.5, customer.wallet)
        self.assertEqual(1004.5, self.pub.till)

        