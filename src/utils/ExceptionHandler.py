def ExceptionHandler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"Validation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
    return wrapper
