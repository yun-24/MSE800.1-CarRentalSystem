
CREATE TABLE users (
                       user_id INT AUTO_INCREMENT PRIMARY KEY,
                       username VARCHAR(50) NOT NULL,
                       password VARCHAR(100) NOT NULL,
                       role ENUM('Customer', 'Admin') NOT NULL,
                       ctime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       utime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE cars (
                      car_id INT AUTO_INCREMENT PRIMARY KEY,
                      make VARCHAR(50) NOT NULL,
                      model VARCHAR(50) NOT NULL,
                      year INT NOT NULL,
                      mileage INT NOT NULL,
                      available_now BOOLEAN NOT NULL,
                      min_rent_period INT NOT NULL,
                      max_rent_period INT NOT NULL,
                      ctime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                      utime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE rentals (
                         rental_id INT AUTO_INCREMENT PRIMARY KEY,
                         car_id INT NOT NULL,
                         user_id INT NOT NULL,
                         start_date DATE NOT NULL,
                         end_date DATE NOT NULL,
                         total_fee DECIMAL(10, 2) NOT NULL,
                         ctime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                         utime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                         FOREIGN KEY (car_id) REFERENCES cars(car_id),
                         FOREIGN KEY (user_id) REFERENCES users(user_id)
);