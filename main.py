def largest_element_in_array(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if largest < arr[i]:
            largest = arr[i]
    return largest
            

arr = [10,555,55,2,5477]
print(largest_element_in_array(arr))