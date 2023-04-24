# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for
# retrieving elements using square brackets syntax.

class MyIterable:
    def __init__(self, iterable):
        self._data = iterable

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        value = self._data[self._index]
        self._index += 1
        return value

    def __getitem__(self, index):
        return self._data[index]


my_iterable = MyIterable([1, 2, 3, 4, 5])

# Iterate over the iterable
for item in my_iterable:
    print(item)

# Get an item by index using square bracket syntax
print(my_iterable[0])  # Output: 1
print(my_iterable[2])  # Output: 3
