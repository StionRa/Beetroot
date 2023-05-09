# In this implementation, we define a Node class to represent a node in the linked list. Each node contains a
# data element and a reference to the next node in the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# The Stack class has a reference to the head of the linked list,
# which is initially set to None to represent an empty stack.
class Steck:
    def __init__(self):
        self.head = None

    # The is_empty method checks if the stack is empty by checking if the head is None.
    def is_empty(self):
        return self.head is None

    # The push method adds an item to the top of the stack by creating a new node with the item as its data element,
    # setting its next reference to the current head of the list, and setting the head of the list to the new node.
    def push(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    # The pop method removes and returns the top item from the stack by checking if the stack is empty, setting a
    # temporary variable to the current head of the list, updating the head of the list to
    # the next node in the list, and returning the data element of the temporary node.
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    # The peek method returns the top item from the stack without removing it by checking if the stack is
    # empty and returning the data element of the head of the list.
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        else:
            return self.head.data

    # The size method returns the number of items in the stack by iterating through the
    # list and counting the number of nodes.
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

