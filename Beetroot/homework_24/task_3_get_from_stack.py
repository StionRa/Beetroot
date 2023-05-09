class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_from_stack(self, value):
        found = False
        temp_stack = Stack()

        while not self.is_empty():
            item = self.pop()
            if item == value and not found:
                found = True
            else:
                temp_stack.push(item)
        if not found:
            raise ValueError(f"{value} not found in stack")

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        return self.items
