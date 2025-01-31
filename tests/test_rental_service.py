import unittest
from datetime import datetime
from unittest import TestCase

from src.services.rental_service import RentalService


class TestRentalService(TestCase):
    def setUp(self):
        self.rental_service = RentalService()

    def test_approve_rental(self):
        self.rental_service.approve_rental(1)

    def test_book_rental(self):
        start_date = datetime.strptime("2024-11-11", '%Y-%m-%d')
        end_date = datetime.strptime( "2024-11-12", '%Y-%m-%d')
        self.rental_service.book_rental(1, 3, start_date, end_date)


if __name__ == "__main__":
    unittest.main()
