from src.database import DatabaseConnection

class RentalRepository:
    def __init__(self, connection=None):
        self.connection = connection if connection else DatabaseConnection().get_connection()

    def add_rental(self, car_id, user_id, start_date, end_date, total_fee):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO rentals (car_id, user_id, start_date, end_date, total_fee, status) VALUES (%s, %s, %s, %s, %s, 'pending')"
            cursor.execute(sql, (car_id, user_id, start_date, end_date, total_fee))
            self.connection.commit()
            return {
                'rental_id': cursor.lastrowid,
                'car_id': car_id,
                'user_id': user_id,
                'start_date': start_date,
                'end_date': end_date,
                'total_fee': total_fee
            }

    def delete_rental(self, rental_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM rentals WHERE rental_id=%s"
            cursor.execute(sql, (rental_id,))
            self.connection.commit()

    def get_rentals_by_user(self, user_id):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM rentals WHERE user_id=%s"
            cursor.execute(sql, (user_id,))
            results = cursor.fetchall()
            rentals = []
            for result in results:
                rentals.append({
                    'rental_id': result['rental_id'],
                    'car_id': result['car_id'],
                    'user_id': result['user_id'],
                    'start_date': result['start_date'],
                    'end_date': result['end_date'],
                    'total_fee': result['total_fee'],
                    'status': result['status']
                })
            return rentals

    def get_all_rentals(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM rentals"
            cursor.execute(sql)
            results = cursor.fetchall()
            rentals = []
            for result in results:
                rentals.append({
                    'rental_id': result['rental_id'],
                    'car_id': result['car_id'],
                    'user_id': result['user_id'],
                    'start_date': result['start_date'],
                    'end_date': result['end_date'],
                    'total_fee': result['total_fee'],
                    'status': result['status']
                })
            return rentals

    def approve_rental(self, rental_id):
        with self.connection.cursor() as cursor:
            # Step 1: Update rental status to 'approved'
            sql = "UPDATE rentals SET status='approved' WHERE rental_id=%s"
            cursor.execute(sql, (rental_id,))

            # Step 2: Get the car_id for the approved rental
            sql_get_car_id = "SELECT car_id FROM rentals WHERE rental_id=%s"
            cursor.execute(sql_get_car_id, (rental_id,))
            car_id = cursor.fetchone()['car_id']

            # Step 3: Update car availability to FALSE
            sql_car = "UPDATE cars SET available_now=FALSE WHERE car_id=%s"
            cursor.execute(sql_car, (car_id,))
            self.connection.commit()

    def reject_rental(self, rental_id):
        with self.connection.cursor() as cursor:
            sql = "UPDATE rentals SET status='rejected' WHERE rental_id=%s"
            cursor.execute(sql, (rental_id,))
            self.connection.commit()
