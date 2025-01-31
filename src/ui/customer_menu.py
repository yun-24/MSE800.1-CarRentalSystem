from src.services.car_service import CarService
from src.services.rental_service import RentalService
from datetime import datetime

from src.ui.MenuABC import MenuABC
from src.utils.Session import Session


class CustomerMenu(MenuABC):
    def __init__(self, car_service=None, rental_service=None):
        self.car_service = car_service if car_service else CarService()
        self.rental_service = rental_service if rental_service else RentalService()
        # Retrieve user_id from session
        self.user_id = Session.get_current_user()['user_id']

    def display(self):
        while True:
            print("\nCustomer Menu")
            print("1. View Cars")
            print("2. Book Rental")
            print("3. View Rentals")
            print("4. Cancel Rental")
            print("5. Logout")
            choice = input("Enter choice: ")

            if choice == '1':
                self.view_cars()
            elif choice == '2':
                self.book_rental()
            elif choice == '3':
                self.view_rentals()
            elif choice == '4':
                self.cancel_rental()
            elif choice == '5':
                Session.logout()  # Clear session
                break
            else:
                print("Invalid choice. Please try again.")

    def view_cars(self):
        # Fetch available cars
        cars = self.car_service.get_available_cars()

        print("\nAvailable Cars:")
        for car in cars:
            print(f"Car ID: {car['car_id']}, Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, "
                  f"Mileage: {car['mileage']}, Available Now: {car['available_now']}, "
                  f"Min Rent Period: {car['min_rent_period']}, Max Rent Period: {car['max_rent_period']}")

    def book_rental(self):
        car_id = input('Enter Car ID: ')
        user_id = self.user_id
        start_date = datetime.strptime(input('Enter Start Date (YYYY-MM-DD): '), '%Y-%m-%d')
        end_date = datetime.strptime(input('Enter End Date (YYYY-MM-DD): '), '%Y-%m-%d')

        rental = self.rental_service.book_rental(car_id, user_id, start_date, end_date)
        if rental:
            print(f"Booking successful! Total fee: ${rental['total_fee']}")
        else:
            print("Booking failed. Please try again.")

    def view_rentals(self):
        user_id = self.user_id
        rentals = self.rental_service.view_rentals(user_id)
        for rental in rentals:
            print(f"Rental ID: {rental['rental_id']}, Car ID: {rental['car_id']}, User ID: {rental['user_id']}, "
                  f"Start Date: {rental['start_date']}, End Date: {rental['end_date']}, Total Fee: ${rental['total_fee']}, "
                  f"Status: {rental['status']}")

    def cancel_rental(self):
        rental_id = input('Enter Rental ID: ')
        self.rental_service.cancel_rental(rental_id)
        print("Rental cancelled successfully.")