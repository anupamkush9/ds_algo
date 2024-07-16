def get_possible_pairs(arr, target):
    arr_len = len(arr)
    count = 0
    for i in range(arr_len):
        for j in range(i+1,arr_len):
            if arr[i]+arr[j] == target:
                count += 1
    return count

l = [1, 5, 7, -1]
target = 6
print(get_possible_pairs(l, target))


# ref
# https://www.geeksforgeeks.org/container-with-most-water/