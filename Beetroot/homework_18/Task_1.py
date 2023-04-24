# Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
# `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
# with enumerate
e = enumerate([1, 2, 3], start=1)
print(e.__next__())
print(e.__next__())
print(e.__next__())


# without enumerate
def with_index(iterable, start=1):
    for key, value in zip(range(start, len(iterable) + start), iterable):
        yield key, value


my_list = [1, 2, 3, 4, 5]
for key, value in with_index(my_list):
    print(f"{key}: {value}")
