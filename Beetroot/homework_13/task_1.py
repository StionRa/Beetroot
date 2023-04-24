# Write a decorator that prints a function with arguments passed to it.
#
# NOTE! It should print the function, not the result of its execution!
def logger(func):
    def wrapper(*args, **kwargs):
        arg_list = []
        print(func.__name__, *args, kwargs)

        # Print positional arguments
        for arg in args:
            arg_list.append(repr(arg))

        # Print keyword arguments
        for key, value in kwargs.items():
            arg_list.append(f"{key}={repr(value)}")

        # Print function and arguments
        arg_str = ', '.join(arg_list)
        print(f"{func.__name__}({arg_str})")

        # Call the decorated function
        return func(*args, **kwargs)

    return wrapper
@logger
def my_func(x, y, z=None):
    return x + y + (z or 0)
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(my_func)
print(square_all)
