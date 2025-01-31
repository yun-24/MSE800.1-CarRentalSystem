import unittest
from unittest import TestCase

from src.ui.customer_menu import CustomerMenu
from src.utils.Session import Session


class TestCustomerMenu(TestCase):
    def setUp(self):
        Session.login('3', 'customer')
        self.customer_menu = CustomerMenu()

    def test_view_rentals(self):
        self.customer_menu.view_rentals()

    def test_view_cars(self):
        self.customer_menu.view_cars()

if __name__ == "__main__":
    unittest.main()


