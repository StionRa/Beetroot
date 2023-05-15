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
