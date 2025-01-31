import sys

import pymysql
import yaml
import os

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        # Read the configuration file
        # config_path = os.path.abspath('config.yaml')
        # print(f"Attempting to open config file at: {config_path}")
        config_file = 'config.yaml'
        if not os.path.isfile(config_file):
            print(f"Error: Configuration file '{config_file}' not found.")
            sys.exit(1)  # Exit the program with an error code
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)

        # Retrieve the database connection details
        db_config = config['database']
        # print(db_config['password'])
        self.connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password= db_config['password'],
            database=db_config['database'],
            cursorclass=pymysql.cursors.DictCursor  # Use DictCursor to get dictionary-like rows
        )

    def get_connection(self):
        return self.connection
