def sort(arr):
    for i in range(len(arr)):
        max = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[max]:
                max = j
        arr[i], arr[max] = arr[max], arr[i]
    return arr


list = [2, 1, 4, 123, 7, 678, 12]
print(sort(list))
