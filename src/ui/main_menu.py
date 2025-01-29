
from src.ui.user_menu import UserMenu

class MainMenu:
    def __init__(self, user_menu=None):
        self.user_menu = user_menu if user_menu else UserMenu()

    def display(self):
        while True:
            print("\nWelcome to the Car Rental System")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.user_menu.register()
            elif choice == '2':
                self.user_menu.login()
            elif choice == '3':
                print("Thank you for using the Car Rental System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")