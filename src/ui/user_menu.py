from src.services.user_service import UserService
from src.ui.MenuFactory import MenuFactory
from src.utils.ExceptionHandler import ExceptionHandler
from src.utils.Session import Session

@ExceptionHandler
class UserMenu:
    def __init__(self, user_service=None, menu_factory=None):
        self.user_service = user_service if user_service else UserService()
        self.menu_factory = menu_factory if menu_factory else MenuFactory()


    def register(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        role = input('Enter role (Customer/Admin): ')

        self.user_service.register_user(username, password, role)
        print(f"User '{username}' registered successfully as a {role}.")


    def login(self):
        username = input('Enter username: ')
        password = input('Enter password: ')

        user = self.user_service.login_user(username, password)
        if user:
            role = user['role']
            # Store user info in session
            Session.login(user['user_id'], role)  # Store user in session


            print(f"Welcome back, {username}! You are logged in as a {role}.")
            menu = self.menu_factory.get_menu(role)  # Use factory to get the menu
            menu.display()
        else:
            print("Login failed. Invalid username or password.")