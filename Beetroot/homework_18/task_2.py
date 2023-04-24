# Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# `start`, `end`, and optional step. Tips: See the documentation for `range` function


for i in range(3, 16, 3):
    print(i)


def in_range(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

for i in in_range(3, 16, 3):
    print(i)
