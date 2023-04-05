# Write a decorator `arg_rules` that validates arguments passed to the function.
#
# A decorator should take 3 arguments:
#
# max_length: 15
#
# type_: str
#
# contains: [] - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
def arg_rules(max_length: int, type_: type, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                # Check argument type
                if not isinstance(arg, type_):
                    print(f"Argument {arg} is not of type {type_}")
                    return False

                # Check argument length
                if len(arg) > max_length:
                    print(f"Argument {arg} exceeds maximum length of {max_length}")
                    return False

                # Check if argument contains required symbols
                if not all(symbol in arg for symbol in contains):
                    print(f"Argument {arg} does not contain required symbols {contains}")
                    return False

            # Call the decorated function if all checks pass
            return func(*args, **kwargs)

        return wrapper

    return decorator

@arg_rules(max_length=10, type_=str, contains=['@'])
def my_func(email):
    print(f"Processing {email}")
    return True
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("S@SH05"))
print(my_func('johndoe05@gmail.com'))