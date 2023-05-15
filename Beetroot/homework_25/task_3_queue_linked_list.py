from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.remove_last()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        last_node = self.items.head
        while last_node.next is not None:
            last_node = last_node.next
        return last_node.data

    def size(self):
        return self.items.size()
