from src.repositories.user_repository import UserRepository
from src.models.user_model import User

class UserService:
    def __init__(self, user_repository=None):
        self.user_repository = user_repository if user_repository else UserRepository()


    def register_user(self, username, password, role):
        # Validate inputs
        # check input, if role is valid
        if not username or not password or role.lower() not in ['customer', 'admin']:
            raise ValueError("Invalid user details.")
        # check if username is unique
        if self.user_repository.find_user_by_username(username):
            raise ValueError("Username already exists")

        # Proceed with registration
        self.user_repository.add_user(username, password, role)

    def login_user(self, username, password):
        result = self.user_repository.find_user(username, password)
        # print(result)
        if result:
            return result
        return None

    def get_user_by_username(self, username):
        user_data = self.user_repository.find_user_by_username(username)
        if user_data:
            return User(user_data['user_id'], user_data['username'], user_data['password'], user_data['role'])
        return None
