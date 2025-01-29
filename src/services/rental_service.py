from src.repositories.rental_repository import RentalRepository

class RentalService:
    def __init__(self, rental_repository=None):
        self.rental_repository = rental_repository if rental_repository else RentalRepository()

    def book_rental(self, car_id, user_id, start_date, end_date):
        return self.rental_repository.add_rental(car_id, user_id, start_date, end_date, (end_date - start_date).days * 100)

    def cancel_rental(self, rental_id):
        self.rental_repository.delete_rental(rental_id)

    def view_rentals(self, user_id):
        return self.rental_repository.get_rentals_by_user(user_id)

    def manage_rentals(self):
        return self.rental_repository.get_all_rentals()

    def approve_rental(self, rental_id):
        self.rental_repository.approve_rental(rental_id)

    def reject_rental(self, rental_id):
        self.rental_repository.reject_rental(rental_id)
