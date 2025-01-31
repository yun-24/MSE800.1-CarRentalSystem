import unittest
from unittest import TestCase

from src.services.rental_service import RentalService


class TestRentalService(TestCase):
    def setUp(self):
        self.rental_service = RentalService()

    def test_approve_rental(self):
        self.rental_service.approve_rental(1)


if __name__ == "__main__":
    unittest.main()