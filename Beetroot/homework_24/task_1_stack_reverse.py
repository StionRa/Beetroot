class Stack:

    # A stack is a data structure that follows the LIFO (last in, first out) principle.
    # It has the following methods:
    # - is_empty: Returns True if the stack is empty, otherwise False.
    # - push: Adds an item to the top of the stack.
    # - pop: Removes and returns the item at the top of the stack.
    # - peek: Returns the item at the top of the stack without removing it.
    # - size: Returns the number of items in the stack.

    def __init__(self):
        # Initializes an empty stack.
        self.items = []

    def is_empty(self):
        # Returns True if the stack is empty, otherwise False.
        return len(self.items) == 0

    def push(self, item):
        # Adds an item to the top of the stack.
        self.items.append(item)

    def pop(self):

        # Removes and returns the item at the top of the stack.
        # Raises an exception if the stack is empty.

        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):

        # Returns the item at the top of the stack without removing it.
        # Raises an exception if the stack is empty.

        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        # Returns the number of items in the stack.
        return len(self.items)

    def __repr__(self):

        # Returns a string representation of the stack, with each item and its corresponding index.

        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self.items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):

        # Returns a string representation of the stack, with each item and its corresponding index.

        return self.__repr__()


def reverse_string(string):
    # The reverse_string function takes a string as input and returns a new string
    # that contains the input string characters in reverse order.
    stack = Stack()
    # It does this by creating a new Stack object, and then iterating over the input string,
    # pushing each character onto the stack.
    for c in string:
        stack.push(c)
    reversed_string = ""
    # Then, it creates an empty string called reversed_string. The function then enters a loop that continues until
    # the stack is empty. In each iteration of the loop, the function pops a character
    # from the stack and appends it to the reversed_string.
    while not stack.is_empty():
        reversed_string += stack.pop()
    # Finally, the function returns the reversed_string.
    return reversed_string
