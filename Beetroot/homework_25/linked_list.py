class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove_first(self):
        if self.head is None:
            raise IndexError("Linked list is empty")
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def remove_last(self):
        if self.head is None:
            raise IndexError("Linked list is empty")
        elif self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            data = current.next.data
            current.next = None
            return data
