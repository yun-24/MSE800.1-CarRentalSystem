from src.ui.customer_menu import CustomerMenu
from src.ui.admin_menu import AdminMenu


class MenuFactory:
    @staticmethod
    def get_menu(role):
        if role.lower() == 'customer':
            return CustomerMenu()
        elif role.lower() == 'admin':
            return AdminMenu()
        else:
            raise ValueError(f"Invalid role: {role}")