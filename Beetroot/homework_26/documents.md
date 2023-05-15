# Binary search using recursion
### This recursive binary_search_recursive function performs a binary search in a sorted array to find the target element. It takes the following parameters:****
    def binary_search_recursive(array, target, left, right):
        if right >= left:
            mid = left + (right - left) // 2
    
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                return binary_search_recursive(array, target, left, mid - 1)
            else:
                return binary_search_recursive(array, target, mid + 1, right)
        else:
            return -1
_left - the left boundary of the search space (initially 0)<br>
right - the right boundary of the search space (initially len(array) - 1)_

The algorithm recursively divides the search space in half and compares the middle element with the desired element. If the value of the middle element is equal to the search element, the index of the middle element is returned. If the value of the middle element is greater than the search element, a recursive search in the left half of the search space is called.
If the value of the middle element is less than the desired element, a recursive search in the right half of the search space is called. If the search space is narrowed to an empty space (right < left), -1 is returned, which means that the desired element is not found.

# Fibonacci search

    def fibonacci_search(array, target):
    fib2 = 0  # n-2 term
    fib1 = 1  # n-1 term
    fib = fib2 + fib1  # current term

    while fib < len(array):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1  # offset for the array

    while fib > 1:
        # Determine the index to be compared
        i = min(offset + fib2, len(array) - 1)

        # If the target element is greater, shift Fibonacci sequence two steps down
        if array[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        # If the target element is smaller, shift Fibonacci sequence one step down
        elif array[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        # If the target element is found, return its index
        else:
            return i

    # Check the last element
    if fib1 == 1 and array[offset + 1] == target:
        return offset + 1

    # If the target element is not found, return -1
    return -1

As for the Fibonacci search algorithm, it is an optimised search algorithm that uses a sequence of Fibonacci numbers to determine the size of the search space and the point where the division should be made. The complexity of the Fibonacci search algorithm is also logarithmic O(log n), similar to binary search. However, the Fibonacci search algorithm can be more efficient Compared to binary search, the Fibonacci search algorithm can be more efficient in some cases, especially when the array is large and has an uneven distribution of elements.

The complexity of the Fibonacci search algorithm is also logarithmic O(log n), where n is the number of elements in the sorted array. This means that the search time grows more slowly with the size of the array.

However, compared to binary search, the Fibonacci search algorithm has additional operations to calculate Fibonacci numbers and determine the dividing point. This can lead to additional computational costs, especially for arrays with a large number of elements.

So, the choice between binary search and Fibonacci search algorithm depends on the specific requirements and properties of the input data. In general, if the array is sorted and has a uniform distribution of elements, binary search is an effective choice. However, if the array has an uneven distribution of elements or if you need to search for a large number of elements, the Fibonacci search algorithm may have advantages in terms of search speed.
