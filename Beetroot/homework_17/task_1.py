# The re module in Python provides support for regular expressions. Regular expressions are a powerful way to
# search for and manipulate text patterns in strings.

import re


class MyClass:
    def __init__(self, email):
        self.email = email
        self.validate()

    @staticmethod
    def is_valid_email(email):
        # Create a regular expression pattern to match email addresses
        # The pattern is explained below
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        # Use the fullmatch method to check if the email matches the pattern exactly
        # If it does, return the match object, otherwise return None
        return re.fullmatch(email_regex, email)

    def validate(self):
        # Check if the email is valid by calling the is_valid_email method
        if not MyClass.is_valid_email(self.email):
            # If the email is invalid, print a message
            print("Invalid email format")


# Create an instance of MyClass with an email address
my_email = MyClass("abc.def@mail..com")
# Print the email address (just to show that it was set correctly)
print(my_email.email)
