# Car Rental System

This is a Car Rental System application that allows users to register, login, view cars, book rentals, and manage rentals. The application follows a clean architecture with separation of concerns.

## Project Structure

- `main.py`: Entry point of the application.
- `src/`: Contains all the source code.
    - `models/`: Data models for users, cars, and rentals.
    - `ui/`: User Interface for the application. Handles displaying information to the user.
    - `repositories/`: Handles database operations.
    - `services/`: Contains business logic.
    - `database.py`: Database connection setup.
- `tests/`: Contains unit tests.
- `docs/`: Documentation.

## How to Run

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
2. Create the database schema (refer to docs folder for SQL script).
3.Run the application:
```bash
python main.py