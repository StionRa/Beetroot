# Importing the 'wraps' decorator from the 'functools' module.
# This decorator is used to preserve the metadata of the original function
# when it's decorated by the wrapper function.
from functools import wraps


# Defining a class 'TypeDecorators' that provides several static methods
# for converting the results of functions to a specified type.
class TypeDecorators:
    # A static method 'to_int' that takes a function as an argument and returns a wrapper function
    # that tries to convert the result of the input function to an integer.
    # If the conversion fails, the wrapper function returns the original result.
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result

        return wrapper

    # A static method 'to_str' that takes a function as an argument and returns a wrapper function
    # that converts the result of the input function to a string using the built-in 'str' function.
    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    # A static method 'to_bool' that takes a function as an argument and returns a wrapper function
    # that tries to convert the result of the input function to a boolean.
    # If the result is a string, the wrapper function compares it to the string 'true' (ignoring case).
    # If the result is not a string, the wrapper function converts it to a boolean using the built-in 'bool' function.
    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return result.lower() == 'true'
            else:
                return bool(result)

        return wrapper

    # A static method 'to_float' that takes a function as an argument and returns a wrapper function
    # that tries to convert the result of the input function to a float.
    # If the conversion fails, the wrapper function returns the original result.
    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result

        return wrapper


# In the to_int and to_float methods, we try to convert the result of the decorated function to an integer or a float,
# respectively, and return the original result if the conversion fails. In the to_bool method, we check if the result
# is a string and convert it to a boolean based on whether it is equal to the string "true" (ignoring case).
# If the result is not a string, we simply convert it to a boolean using the built-in bool() function.
# The to_str method simply converts the result to a string using the str() function.

@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
