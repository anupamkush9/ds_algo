def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
arr = [0, 5, 12, 77, 88, 55]
print("Before sorting array : ", arr)
reverse_array(arr)
print("After sorting array : ", arr)
