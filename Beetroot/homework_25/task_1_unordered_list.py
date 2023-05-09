# Node class represents a single node in the linked list. It has two attributes: data and next.
# The data attribute stores the actual data of the node, while the next attribute is a reference to the next
# node in the list. If next is None, it means that the current node is the last node in the list.
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None


# UnorderedList class represents the linked list itself. It has only one attribute: head, which is a reference
# to the first node in the list. If head is None, it means that the list is empty.
class UnorderedList:
    def __init__(self):
        self.head = None

    # is_empty() method checks if the list is empty.
    def is_empty(self):
        return self.head is None

    # add(item) method adds a new item to the beginning of the list.
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    # size() method returns the number of nodes in the list.
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    # print_list() method prints all the items in the list.
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

    # search(item) method searches for an item in the list and returns True if it is found, otherwise False.
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    # remove(item) method removes the first occurrence of an item from the list.
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    # append(item) method adds a new item to the end of the list.
    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

    # index(item) method returns the index of the first occurrence of an item in the list.
    def index(self, item):
        current = self.head
        index = 0
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
                index += 1
        if found:
            return index
        else:
            raise ValueError(f"{item} not in list")

    # pop(pos=None) method removes and returns the last item in the list.
    # If the pos argument is provided, it removes and returns the item at the given position.
    def pop(self, pos=None):
        if pos is None:
            if self.head is None:
                raise IndexError("pop from empty list")
            else:
                current = self.head
                previous = None
                while current.next is not None:
                    previous = current
                    current = current.next
                if previous is None:
                    self.head = None
                else:
                    previous.next = None
                return current.data
        else:
            if pos < 0:
                pos += self.size()
            if pos < 0 or pos >= self.size():
                raise IndexError(f"pop index {pos} out of range")
            current = self.head
            previous = None
            index = 0
            while index < pos:
                previous = current
                current = current.next
                index += 1
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            return current.data

    # insert(pos, item) method inserts a new item at the given position in the list.
    def insert(self, pos, item):
        if pos < 0:
            pos += self.size()
        if pos < 0 or pos > self.size():
            raise IndexError(f"insert index {pos} out of range")
        temp = Node(item)
        if pos == 0:
            temp.next = self.head
            self.head = temp
        else:
            current = self.head
            previous = None
            index = 0
            while index < pos:
                previous = current
                current = current.next
                index += 1
            temp.next = current
            previous.next = temp

    # slice(start, stop) method returns a new list that contains a copy of the items from the start position up to
    # but not including the stop position. If start is negative, it is interpreted as an offset from the end of the
    # list. If stop is None or greater than the size of the list, it is interpreted as the end of the list.
    # If stop is negative, it is interpreted as an offset from the end of the list. If start is greater than or
    # equal to stop, an empty list is returned.
    def slice(self, start, stop):
        if start < 0:
            start += self.size()
        if stop is None or stop > self.size():
            stop = self.size()
        if stop < 0:
            stop += self.size()
        if start >= stop:
            return UnorderedList()
        current = self.head
        index = 0
        while index < start:
            current = current.next
            index += 1
        new_list = UnorderedList()
        while index < stop:
            new_list.append(current.data)
            current = current.next
            index += 1
        return new_list

