# the math module in Python provides access to various mathematical functions and constants.
# It is a built-in module, which means you don't need to install any additional libraries to use it.
import math


# A class in Python is a blueprint for creating objects that have certain attributes
# (data) and methods (functions) associated with them.
#
# A class is defined using the class keyword, followed by the name of the class (usually in CamelCase format),
# and a colon. The class definition typically includes a constructor (__init__ method) and other
# methods and attributes as needed.
class Fraction:

    # __init__ is a special method in Python classes that is called when an object of that class is
    # created. It is also known as the constructor method. The purpose of __init__ is to initialize
    # the attributes of the object.
    #
    # When a new object of a class is created, Python automatically calls the __init__ method with the
    # newly created object as its first argument. The remaining arguments passed to the constructor are used
    # to initialize the object's attributes.
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator can't be zero")
        self.numerator = numerator
        self.denominator = denominator

    # __str__ is a special method in Python classes that is used to return a human-readable string representation of an
    # object. The purpose of __str__ is to provide a string representation of an object that is suitable for
    # display to end-users.
    #
    # When you call the built-in str() function on an object, Python will first look for a __str__
    # method on that object and use it to return a string representation of the object.
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        # return f"{self.numerator}/{self.denominator}"
        gcd = math.gcd(self.numerator, self.denominator)
        simplified_numerator = self.numerator // gcd
        simplified_denominator = self.denominator // gcd
        return f"{simplified_numerator}/{simplified_denominator}"

    # __repr__ is a special method in Python classes that is used to return a string representation of an object.
    # The purpose of __repr__ is to provide a concise, unambiguous string representation of an object that can be
    # used to recreate the object. This string representation is typically used for debugging and logging purposes.
    #
    # __repr__ should return a string that, when passed to Python's built-in eval() function, will recreate the object.
    # The string should be a valid Python expression that evaluates to an object of the same type as the original
    # object.
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    # __add__ is a special method in Python used to define the behavior of the addition operator + when
    # applied to objects of a class. It is called when the object is on the left-hand side of the addition operator +.
    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    # __sub__ is a special method in Python used to define the behavior of the subtraction operator - when applied to
    # objects of a class. It is called when the object is on the left-hand side of the subtraction operator -.
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    # __mul__ is a special method in Python used to define the behavior of the multiplication operator * when applied
    # to objects of a class. It is called when the object is on the left-hand side of the multiplication operator *
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    # __truediv__ is a special method in Python used to define the behavior of the division operator / when applied
    # to objects of a class. It is called when the object is on the left-hand side of the division operator /.
    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    # __eq__ is a special method in Python that stands for "equal". It's used for implementing the equality
    # comparison operator (==) for a class.
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.numerator * other.denominator == other.numerator * self.denominator

    # __ne__ is a special method in Python that stands for "not equal". It's used for implementing
    # the not equal comparison operator (!=) for a class.
    def __ne__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return not self == other

    # __lt__ is a special method in Python that stands for "less than". It's used for implementing the less
    # than comparison operator (<) for a class.
    def __lt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    # __le__ is a special method in Python that stands for "less than or equal to". It's used for implementing
    # the less than or equal to comparison operator (<=) for a class.
    def __le__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.numerator * other.denominator <= other.numerator * self.denominator

    # __gt__ is a special method in Python that stands for "greater than". It's used for
    # implementing the greater than comparison operator (>) for a class.
    def __gt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.numerator * other.denominator > other.numerator * self.denominator

    # __ge__ is a special method in Python that stands for "greater than or equal to". It's used for implementing
    # the greater than or equal to comparison operator (>=) for a class.
    def __ge__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.numerator * other.denominator >= other.numerator * self.denominator


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))  # True

    a = Fraction(1, 2)
    b = Fraction(1, 4)
    c = a + b
    print(c)

    w = Fraction(10, 1)
    v = Fraction(10, 1)
    u = w + v
    print(u)
