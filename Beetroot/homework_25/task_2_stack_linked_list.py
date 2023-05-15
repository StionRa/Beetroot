from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.remove_first()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.head.data

    def size(self):
        return self.items.size()
