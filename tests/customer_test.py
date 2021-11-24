import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink('Whisky', 5.00, True, 1.00)
        self.drink2 = Drink('Espresso Martini', 7.00, True, 3.00)
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27, 4.00)
        
    def test_customer_has_name(self):
        self.assertEqual("Stephen O'Reilly", self.customer.name)

    def test_customer_has_stomach(self):
        self.assertEqual(2, len(self.customer.stomach))

    def test_customer_has_wallet(self):
        self.assertEqual(6.00, self.customer.wallet)
    
    def test_customer_can_afford_drink(self):
        self.assertEqual(True, self.customer.can_afford_drink(self.drink1))
        self.assertEqual(False, self.customer.can_afford_drink(self.drink2))

    def test_customer_can_afford_food(self):
        self.food1 = Food("Crisps", 1.00, 0.5)
        self.food2 = Food("Caviar", 15.00, 1)
        self.assertEqual(True, self.customer.can_afford_food(self.food1))
        self.assertEqual(False, self.customer.can_afford_food(self.food2))

    def test_customer_get_drunkeness(self):
        self.assertEqual(4.00, self.customer.get_drunkeness())

    def test_down_drink(self):
        self.customer.down_drink(self.drink1)
        self.assertEqual(5.00, self.customer.drunkeness)
        self.assertEqual(3, len(self.customer.stomach))

    def test_eat_food(self):
        self.food = Food("Crisps", 1.00, 0.5)
        self.customer.eat_food(self.food)
        self.assertEqual(3.5, self.customer.drunkeness)