from src.repositories.user_repository import UserRepository
from src.models.user_model import User

class UserService:
    def __init__(self, user_repository=None):
        self.user_repository = user_repository if user_repository else UserRepository()


    def register_user(self, username, password, role):
        # Check if user already exists
        if self.user_repository.find_user_by_username(username):
            return False

        # Proceed with registration
        self.user_repository.add_user(username, password, role)
        return True

    def login_user(self, username, password):
        result = self.user_repository.find_user(username, password)
        # print(result)
        if result:
            return result['role']
        return None

    def get_user_by_username(self, username):
        user_data = self.user_repository.find_user_by_username(username)
        if user_data:
            return User(user_data['user_id'], user_data['username'], user_data['password'], user_data['role'])
        return None
