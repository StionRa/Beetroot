import random
import timeit


def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1


array_1 = [random.randint(1, 100) for _ in range(100)]
array_2 = [random.randint(1, 10000) for _ in range(10000)]

linear_search_time = []
binary_search_times = []

for _ in range(3):
    linear_search_times = timeit.timeit(lambda: linear_search(array_1, 50), number=10000)
    binary_search_time = timeit.timeit(lambda: binary_search(sorted(array_1), 50), number=10000)
    linear_search_times.append(linear_search_time)
    binary_search_times.append(binary_search_time)

# Виводимо результати для першого масиву
print("Перший масив (100 елементів):")
print("Лінійний пошук: середній час -", sum(linear_search_time) / len(linear_search_time))
print("Бінарний пошук: середній час -", sum(binary_search_times) / len(binary_search_times))

