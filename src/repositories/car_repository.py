from src.database import DatabaseConnection


class CarRepository:
    def __init__(self, connection=None):
        self.connection = connection if connection else DatabaseConnection().get_connection()

    def add_car(self, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO cars (make, model, year, mileage, available_now, min_rent_period, max_rent_period) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (make, model, year, mileage, available_now, min_rent_period, max_rent_period))
            self.connection.commit()

    def update_car(self, car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        with self.connection.cursor() as cursor:
            sql = "UPDATE cars SET make=%s, model=%s, year=%s, mileage=%s, available_now=%s, min_rent_period=%s, max_rent_period=%s WHERE car_id=%s"
            cursor.execute(sql, (make, model, year, mileage, available_now, min_rent_period, max_rent_period, car_id))
            self.connection.commit()

    def delete_car(self, car_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM cars WHERE car_id=%s"
            cursor.execute(sql, (car_id,))
            self.connection.commit()

    def get_all_cars(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM cars"
            cursor.execute(sql)
            results = cursor.fetchall()
            cars = []
            for result in results:
                cars.append({
                    'car_id': result['car_id'],
                    'make': result['make'],
                    'model': result['model'],
                    'year': result['year'],
                    'mileage': result['mileage'],
                    'available_now': result['available_now'],
                    'min_rent_period': result['min_rent_period'],
                    'max_rent_period': result['max_rent_period']
                })
            return cars

    def get_available_cars(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM cars WHERE available_now = TRUE"
            cursor.execute(sql)
            results = cursor.fetchall()
            return [dict(result) for result in results]