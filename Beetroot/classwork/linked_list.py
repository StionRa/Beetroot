class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                return current_node
            current_node = current_node.next
        return None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, value):
        current_node = self.head
        if current_node is not None and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node is not None and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def find_all(self, value):
        indexes = []
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.data == value:
                indexes.append(index)
            current_node = current_node.next
            index += 1
        return indexes


linked_list = LinkedList()
linked_list.append(1)
linked_list.append("2")
linked_list.append("Stas")
linked_list.append(2)
linked_list.append(2)
linked_list.append(2)

print(linked_list.find_all(2))
