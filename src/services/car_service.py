from src.repositories.car_repository import CarRepository

class CarService:
    def __init__(self, car_repository=None):
        self.car_repository = car_repository if car_repository else CarRepository()

    def add_car(self, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        self.car_repository.add_car(make, model, year, mileage, available_now, min_rent_period, max_rent_period)

    def update_car(self, car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        self.car_repository.update_car(car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period)

    def delete_car(self, car_id):
        self.car_repository.delete_car(car_id)

    def get_all_cars(self):
        return self.car_repository.get_all_cars()

    def get_available_cars(self):
        return self.car_repository.get_available_cars()