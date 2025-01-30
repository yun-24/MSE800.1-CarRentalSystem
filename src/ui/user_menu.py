from src.services.user_service import UserService
from src.ui.MenuFactory import MenuFactory


class UserMenu:
    def __init__(self, user_service=None, menu_factory=None):
        self.user_service = user_service if user_service else UserService()
        self.menu_factory = menu_factory if menu_factory else MenuFactory()


    def register(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        role = input('Enter role (Customer/Admin): ')

        try:
            self.user_service.register_user(username, password, role)
            print(f"User '{username}' registered successfully as a {role}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def login(self):
        username = input('Enter username: ')
        password = input('Enter password: ')

        role = self.user_service.login_user(username, password)
        if role:
            print(f"Welcome back, {username}! You are logged in as a {role}.")
            menu = self.menu_factory.get_menu(role)  # Use factory to get the menu
            menu.display()
        else:
            print("Login failed. Invalid username or password.")