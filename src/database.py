import pymysql
import yaml

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        # Read the configuration file
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
