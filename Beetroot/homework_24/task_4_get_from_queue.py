class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_from_queue(self, value):
        found = False
        temp_queue = Queue()

        while not self.is_empty():
            item = self.dequeue()
            if item == value and not found:
                found = True
            else:
                temp_queue.enqueue(item)

        if not found:
            raise ValueError(f"{value} not found in queue")

        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())

        return self.items
