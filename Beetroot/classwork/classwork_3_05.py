import timeit
import random


# def find_min_slow(numbers):
#     min_num = numbers[0]
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if numbers[j] < min_num:
#                 min_num = numbers[j]
#     return min_num
#
#
# def find_min_fast(numbers):
#     min_num = numbers[0]
#     for num in numbers:
#         if num < min_num:
#             min_num = num
#     return min_num
#
#
# # Test on an array of 10 elements
# arr_10 = [random.randint(0, 10) for _ in range(10)]
#
# time_slow_10 = timeit.timeit(lambda: find_min_slow(arr_10), number=10)
# time_fast_10 = timeit.timeit(lambda: find_min_fast(arr_10), number=10)
#
# print(f"Time taken by find_min_slow on 10 elements: {time_slow_10}")
# print(f"Time taken by find_min_fast on 10 elements: {time_fast_10}")
# print("")
#
# # Test on an array of 100 elements
# arr_100 = [random.randint(0, 10) for _ in range(100)]
#
# time_slow_100 = timeit.timeit(lambda: find_min_slow(arr_100), number=100)
# time_fast_100 = timeit.timeit(lambda: find_min_fast(arr_100), number=100)
#
# print(f"Time taken by find_min_slow on 100 elements: {time_slow_100}")
# print(f"Time taken by find_min_fast on 100 elements: {time_fast_100}")
# print("")
#
# # Test on an array of 1000 elements
# arr_1000 = [random.randint(0, 10) for _ in range(1000)]
#
# time_slow_1000 = timeit.timeit(lambda: find_min_slow(arr_1000), number=1000)
# time_fast_1000 = timeit.timeit(lambda: find_min_fast(arr_1000), number=1000)
#
# print(f"Time taken by find_min_slow on 1000 elements: {time_slow_1000}")
# print(f"Time taken by find_min_fast on 1000 elements: {time_fast_1000}")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Test with random arrays of different sizes
arr_10 = [random.randint(0, 10) for _ in range(10)]
arr_100 = [random.randint(0, 10) for _ in range(100)]
arr_1000 = [random.randint(0, 10) for _ in range(1000)]

# Measure time taken by bubble_sort on different sized arrays
time_bubble_10 = timeit.timeit(lambda: bubble_sort(arr_10), number=10)
time_bubble_100 = timeit.timeit(lambda: bubble_sort(arr_100), number=100)
time_bubble_1000 = timeit.timeit(lambda: bubble_sort(arr_1000), number=1000)

# Measure time taken by list.sort() on different sized arrays
time_sort_10 = timeit.timeit(lambda: sorted(arr_10), number=10)
time_sort_100 = timeit.timeit(lambda: sorted(arr_100), number=100)
time_sort_1000 = timeit.timeit(lambda: sorted(arr_1000), number=1000)

# Print results
print("Results for bubble_sort:")
print(f"Time taken by bubble_sort on 10 elements: {time_bubble_10}")
# print(f"Time taken by bubble_sort on 100 elements: {time_bubble_100}")
# print(f"Time taken by bubble_sort on 1000 elements: {time_bubble_1000}")
# print("")
#
# print("Results for list.sort():")
# print(f"Time taken by list.sort() on 10 elements: {time_sort_10}")
# print(f"Time taken by list.sort() on 100 elements: {time_sort_100}")
# print(f"Time taken by list.sort() on 1000 elements: {time_sort_1000}")
