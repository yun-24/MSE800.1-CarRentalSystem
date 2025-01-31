import unittest
from unittest import TestCase

from src.services.user_service import UserService


class TestUserService(TestCase):
    def setUp(self):
        self.user_service = UserService()

    @unittest.skip("Run only the first time")
    def test_register_user_success(self):
        # Call the method
        result = self.user_service.register_user("test", "test", "customer")
        self.assertEqual(None, result)

    def test_register_user_already_exists(self):
        # Call the  method
        with self.assertRaises(ValueError) as context:
            self.user_service.register_user("test", "test", "customer")

        self.assertEqual(str(context.exception), "Username already exists")


if __name__ == "__main__":
    unittest.main()