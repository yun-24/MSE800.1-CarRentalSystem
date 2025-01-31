import unittest
from unittest import TestCase

from src.services.car_service import CarService


class TestCarService(TestCase):
    def setUp(self):
        self.car_service = CarService()

    def test_add_car(self):
        self.car_service.add_car("MM", "m", 1990, 100, True, 1, 11)

if __name__ == "__main__":
    unittest.main()