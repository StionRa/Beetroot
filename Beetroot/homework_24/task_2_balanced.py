from task_1_stack_reverse import Stack


def is_balanced(expression):
    stack = Stack()
    # The is_balanced function takes a string expression as input and returns a boolean indicating whether its
    # parentheses, braces, and curly brackets are balanced or not.
    # The function first creates a new Stack object. It then iterates over each character in the input string.
    for char in expression:
        if char in ["(", "{", "["]:
            # If the character is an opening parenthesis, brace, or curly bracket, the function
            # pushes it onto the stack.
            stack.push(char)
        elif char in [")", "}", "]"]:
            # If it is a closing parenthesis, brace, or curly bracket, the function checks whether the stack is empty.
            if stack.is_empty():
                # If it is, this means there is no matching opening character, so the function immediately returns
                # False.
                return False
            else:
                # Otherwise, the function peeks at the top of the stack to see if the opening character matches
                # the closing character.
                # If it does, the function pops the opening character off the stack.
                top = stack.peek()
                if (char == ")" and top == "(") or \
                        (char == "}" and top == "{") or \
                        (char == "]" and top == "["):
                    stack.pop()
                else:
                    # If it doesn't, this means the characters are not balanced, so the function returns False.
                    return False
                # After iterating over all characters, the function checks whether the stack is empty. If it is, this
                # means all opening characters had a matching closing character, so the function returns True.
                # If the stack is not empty, this means there are unmatched opening characters, so the function
                # returns False.
    return stack.is_empty()
