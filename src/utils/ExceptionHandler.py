def ExceptionHandler(cls):
    """Class-level decorator to handle exceptions for all methods."""
    for name, method in cls.__dict__.items():
        if callable(method):  # Check if it's a method
            setattr(cls, name, _handle_exceptions(method))
    return cls

def _handle_exceptions(func):
    """Wrap a method with exception handling and logging."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"Validation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
    return wrapper
