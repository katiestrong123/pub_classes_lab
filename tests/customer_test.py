import unittest
from src.customer import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Bill Billson", 60.56, 63)

    def test_customer_has_name(self):
        self.assertEqual("Bill Billson", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(60.56, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(63, self.customer.age)

    @unittest.skip("")
    def test_customer_can_buy_drink(self):
        pass 


