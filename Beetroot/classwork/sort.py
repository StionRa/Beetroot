import random
import timeit
import csv
import random

# random_list = random.sample(range(10000001), 10000000)  # Генеруємо 1000 унікальних чисел в діапазоні 0-1000
#
# # Запис списку в файл CSV
# with open('test.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(random_list)


with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    x = [row[0] for row in csv_reader]


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


execution_time = timeit.timeit(lambda: bubble_sort(x), number=5)
print(f"Час виконання bubble_sort: {execution_time:.6f} секунд")


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


execution_time = timeit.timeit(lambda: insertion_sort(x), number=5)
print(f"Час виконання insertion_sort: {execution_time:.6f} секунд")


# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


execution_time = timeit.timeit(lambda: selection_sort(x), number=5)
print(f"Час виконання selection_sort: {execution_time:.6f} секунд")


# Merge Sort
def merge_sort_light(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort_light(left_half)
        merge_sort_light(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


execution_time = timeit.timeit(lambda: merge_sort_light(x), number=5)
print(f"Час виконання merge_sort_light: {execution_time:.6f} секунд")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


execution_time = timeit.timeit(lambda: merge_sort(x), number=5)
print(f"Час виконання merge_sort: {execution_time:.6f} секунд")


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


execution_time = timeit.timeit(lambda: quick_sort(x), number=5)
print(f"Час виконання quick_sort: {execution_time:.6f} секунд")
#
#
# # def counting_sort(arr):
# #     # Знайти максимальне значення у списку
# #     max_value = max(arr)
# #
# #     # Створити масив підрахунків зі значеннями 0
# #     counts = [0] * (max_value + 1)
# #
# #     # Підрахувати кількість входжень кожного елемента
# #     for num in arr:
# #         counts[int(num)] += 1
# #
# #     # Створити відсортований список
# #     sorted_arr = []
# #     for i in range(len(counts)):
# #         sorted_arr.extend([i] * counts[i])
# #
# #     return sorted_arr
# #
# # execution_time = timeit.timeit(lambda: counting_sort(x), number=5)
# # print(f"Час виконання counting_sort: {execution_time:.6f} секунд")
