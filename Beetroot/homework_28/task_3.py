import random
import time


def quicksort(arr, partition_limit=10):
    # Main function to perform quicksort on the input array
    _quicksort(arr, 0, len(arr) - 1, partition_limit)


def _quicksort(arr, low, high, partition_limit):
    # Recursive function to perform quicksort on the input array within the given low and high bounds
    if low < high:
        if high - low < partition_limit:
            # If the sublist is small, apply insertion sort instead of further partitioning
            insertion_sort(arr, low, high + 1)
        else:
            # Otherwise, perform partitioning and recursively sort the sublists
            pivot = partition(arr, low, high)
            _quicksort(arr, low, pivot - 1, partition_limit)
            _quicksort(arr, pivot + 1, high, partition_limit)


def partition(arr, low, high):
    # Function to partition the array and return the pivot index

    # Choose the pivot index
    pivot_index = choose_pivot(low, high)
    pivot_value = arr[pivot_index]

    # Move the pivot to the right end of the sublist
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Perform partitioning
    i = low
    for j in range(low, high):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Move the pivot to its final position
    arr[i], arr[high] = arr[high], arr[i]
    return i


def choose_pivot(low, high):
    # Function to choose the pivot index as the middle element between the low and high bounds
    return (low + high) // 2


def insertion_sort(arr, start, end):
    # Function to perform insertion sort on the sublist from the start to end indices
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


list_sizes = [1000, 10000, 100000]  # Different list sizes to test
partition_limits = [10, 50, 100]  # Different partition limits to test

for size in list_sizes:
    for limit in partition_limits:
        # Generate a random list of integers
        arr = [random.randint(1, size) for _ in range(size)]

        # Measure the execution time
        start_time = time.time()
        quicksort(arr, partition_limit=limit)
        end_time = time.time()

        # Print the results
        print(f"List size: {size}, Partition limit: {limit}, Execution time: {end_time - start_time:.6f} seconds")


"""This script implements the quicksort algorithm with an optimization of using insertion sort for small sublists. 
Here's a breakdown of what each part does:

quicksort function: This is the entry point for the quicksort algorithm. It calls the _quicksort function with the 
initial low and high bounds of the array.

_quicksort function: This recursive function performs the actual quicksort algorithm. It checks if the difference 
between the high and low bounds is less than the partition limit. If it is, it applies the insertion sort algorithm 
to the sublist. Otherwise, it selects a pivot using the choose_pivot function, performs partitioning using the 
partition function, and recursively calls _quicksort for the left and right sublists.

partition function: This function takes the input array, low and high bounds, and performs the partitioning step of 
the quicksort algorithm. It chooses the pivot index using the choose_pivot function, moves the pivot element to the 
right end of the sublist, and performs the partitioning by swapping elements based on their values relative to the 
pivot. Finally, it moves the pivot element to its final position and returns the pivot index.

choose_pivot function: This function takes the low and high bounds and chooses the pivot index as the middle element 
between them.

insertion_sort function: This function performs the insertion sort algorithm on a sublist of the array. It takes the 
start and end indices of the sublist and iteratively inserts each element in its correct position within the sublist.

The script provides a way to sort a random list of integers using the quicksort algorithm with the insertion sort 
optimization for small sublists. By analyzing the execution time with different partition limits for various list 
sizes, you can observe how the choice of the partition limit affects the performance of the algorithm."""
