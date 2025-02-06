# Car Rental System

A console-based car rental system with two types of users: Customers and Admins. Customers can view and book cars, while Admins manage the car inventory and rental requests.

## Project Structure

- `main.py`: Entry point of the application.
- `src/`: Contains all the source code.
- `tests/`: Contains unit tests.
- `docs/`: Documentation.

## How to Run

### Prerequisites: 

- Python 3.10+, 
- MySQL
- required Python packages (`requirements.txt`).

### Setup Instructions

1. Create the Database. Refer to the SQL script in the `docs/` folder to create the database schema.
2. Configure Database Connection. Update your database details in`config.yaml`.

### Release Build 

For macOS and Windows, a pre-built executable is available. If you encounter issues, you can always run the system from the source code.

### Run form source 

1. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
   
2. Run the Application
  ```bash
   python main.py
   ```