def container_with_most_water(arr):
    max_contained_water = 0
    left = 0
    right = len(arr)-1
    while(left < right):
        height = min(arr[left], arr[right])
        width = right - left
        current_water = height * width
        max_contained_water = max(max_contained_water, current_water)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_contained_water

# l = [1, 5, 4, 3]
l = [3, 1, 2, 4, 5]
print(container_with_most_water(l))


# ref
# https://www.geeksforgeeks.org/container-with-most-water/