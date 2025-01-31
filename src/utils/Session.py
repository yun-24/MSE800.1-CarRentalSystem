
class Session:
    current_user = None  # Stores user_id and role

    @classmethod
    def login(cls, user_id, role):
        cls.current_user = {'user_id': user_id, 'role': role}

    @classmethod
    def logout(cls):
        cls.current_user = None

    @classmethod
    def get_current_user(cls):
        return cls.current_user