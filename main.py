def get_maximum_trapping_water(arr):
    left_max_boundry = []
    right_max_boundry = []
    trapped_water_arr = []
    for i in range(len(arr)):
        left_max_boundry.append(max(arr[:i+1]))
    for i in range(len(arr)):
        right_max_boundry.append(max(arr[i:]))
    for i in range(len(arr)):
        current_water = min(left_max_boundry[i], right_max_boundry[i]) - arr[i]
        trapped_water_arr.append(current_water)
    print("left_max_boundry::",left_max_boundry)
    print("right_max_boundry::",right_max_boundry)
    print("Initial block arr::",arr)
    print("trapped_water_arr::",trapped_water_arr)
    return sum(trapped_water_arr)


# arr = [3, 0, 1, 0, 4, 0, 2]
arr = [3, 0, 2, 0, 4]
print(get_maximum_trapping_water(arr))

# ref : https://www.geeksforgeeks.org/trapping-rain-water/