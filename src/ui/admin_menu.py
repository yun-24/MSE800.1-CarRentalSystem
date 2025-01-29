from src.services.car_service import CarService
from src.services.rental_service import RentalService

class AdminMenu:
    def __init__(self, car_service=None, rental_service=None):
        self.car_service = car_service if car_service else CarService()
        self.rental_service = rental_service if rental_service else RentalService()

    def display(self):
        while True:
            print("\nAdmin Menu")
            print("1. Add Car")
            print("2. Update Car")
            print("3. Delete Car")
            print("4. Manage Rentals")
            print("5. Logout")
            choice = input("Enter choice: ")

            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.update_car()
            elif choice == '3':
                self.delete_car()
            elif choice == '4':
                self.manage_rentals()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_car(self):
        car_id = input('Enter Car ID: ')
        make = input('Enter Make: ')
        model = input('Enter Model: ')
        year = int(input('Enter Year: '))
        mileage = int(input('Enter Mileage: '))
        available_now = input('Is Available Now (True/False): ').lower() == 'true'
        min_rent_period = int(input('Enter Minimum Rent Period: '))
        max_rent_period = int(input('Enter Maximum Rent Period: '))

        self.car_service.add_car(car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period)
        print('Car added successfully!')

    def update_car(self):
        car_id = input('Enter Car ID: ')
        make = input('Enter Make: ')
        model = input('Enter Model: ')
        year = int(input('Enter Year: '))
        mileage = int(input('Enter Mileage: '))
        available_now = input('Is Available Now (True/False): ').lower() == 'true'
        min_rent_period = int(input('Enter Minimum Rent Period: '))
        max_rent_period = int(input('Enter Maximum Rent Period: '))

        self.car_service.update_car(car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period)
        print('Car updated successfully!')

    def delete_car(self):
        car_id = input('Enter Car ID: ')
        self.car_service.delete_car(car_id)
        print('Car deleted successfully!')


    def manage_rentals(self):
        rentals = self.rental_service.manage_rentals()
        for rental in rentals:
            print(f'Rental ID: {rental["rental_id"]}, Car ID: {rental["car_id"]}, User ID: {rental["user_id"]}, Start Date: {rental["start_date"]}, End Date: {rental["end_date"]}, Total Fee: {rental["total_fee"]}')

        action = input('Enter action (approve/reject): ')
        rental_id = input('Enter Rental ID to approve/reject: ')

        if action == 'approve':
            self.rental_service.approve_rental(rental_id)
            print('Rental request approved.')
        elif action == 'reject':
            self.rental_service.reject_rental(rental_id)
            print('Rental request rejected.')
        else:
            print('Invalid action. Please try again.')
