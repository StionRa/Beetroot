def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bidirectional_bubble_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break

        swapped = False
        right -= 1

        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        left += 1
    return arr


"""A modified bubble sort moving in both directions can be useful in the following cases:

When the list to be sorted is already nearly sorted, or contains a large number of items that are in their places. In 
this case, using a conventional bubble sort, you would have to make many unnecessary passes to move the items to 
their places. The modified version reduces the number of passes, improving performance.

When a list contains items arranged in both ascending and descending order. Conventional bubble sorting is effective 
only when the highest item is moved to the end of the list on each pass. If the list contains elements arranged in an 
unordered order, but with some elements at the beginning of the list and some at the end, a modified version of 
sorting can effectively move elements both to their places at the beginning of the list and to their places at the 
end of the list.

In general, modified bubble sorting can be applied when list items are expected to move in different directions, 
and when there is a need to improve performance in cases where conventional bubble sorting may be inefficient."""
