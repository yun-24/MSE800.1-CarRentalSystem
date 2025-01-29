class Rental:
    def __init__(self, rental_id, car_id, user_id, start_date, end_date, total_fee, status='pending'):
        self.rental_id = rental_id
        self.car_id = car_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_fee = total_fee
        self.status = status
