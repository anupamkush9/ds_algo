def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(binary_search([0, 5, 12, 77, 88], -4))


# ref for time complexity
# https://stackoverflow.com/questions/8185079/how-to-calculate-binary-search-complexity