from abc import ABC, abstractmethod

class MenuABC(ABC):

    @abstractmethod
    def display(self):
        """Display the menu and handle user input."""
        pass