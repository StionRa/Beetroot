# In this implementation, we define a Node class to represent a node in the linked list. Each node contains a
# data element and a reference to the next node in the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# The Queue class has references to both the head and tail of the linked list, which are initially set to
# None to represent an empty queue.
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # The is_empty method checks if the queue is empty by checking if the head is None.
    def is_empty(self):
        return self.head is None

    # The enqueue method adds an item to the back of the queue by creating a new node with the item as its data element,
    # setting its next reference to None, updating the next reference of the current tail node (if it exists)
    # to the new node, and setting the tail reference to the new node.
    def enqueue(self, item):
        temp = Node(item)
        if self.tail is None:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp

    # The dequeue method removes and returns the front item from the queue by checking if the queue is empty, setting a
    # temporary variable to the current head of the list, updating the head of the list to the next node in the list,
    # updating the tail reference to None if the head is None, and returning the data element of the temporary node.
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        else:
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return temp.data

    # The peek method returns the front item from the queue without removing it by checking if the queue is
    # empty and returning the data element of the head of the list.
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        else:
            return self.head.data

    # The size method returns the number of items in the queue by iterating
    # through the list and counting the number of nodes.
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

