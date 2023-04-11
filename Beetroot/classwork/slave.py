from time import time
from functools import wraps


def before_and_after(func):
    """Decorator that prints 'Before' before the function is called and 'After' after the function is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper


def execution_time(func):
    """Decorator that prints the execution time of the function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Execution time: {end_time - start_time:.5f} seconds")
        return result
    return wrapper


# Option 1: Assigning the decorated functions to variables
@before_and_after
def func1():
    """Function 1"""
    print("Function 1 is called")


@execution_time
def func2():
    """Function 2"""
    for i in range(10000000):
        pass


# Option 2: Using @ to apply the decorators
@before_and_after
def func3():
    """Function 3"""
    print("Function 3 is called")


@execution_time
def func4():
    """Function 4"""
    for i in range(10000000):
        pass


# Option 3: Using @wraps to preserve the original function's metadata
@execution_time
@before_and_after
def func5():
    """Function 5"""
    print("Function 5 is called")


# Print function metadata
print(func1.__doc__, func1.__name__)
print(func2.__doc__, func2.__name__)
print(func3.__doc__, func3.__name__)
print(func4.__doc__, func4.__name__)
print(func5.__doc__, func5.__name__)
print(func1())
print(func2())
print(func3())
print(func4())
print(func5())