# largest subarray of sum k by sliding window

def get_largest_subarray_of_sum_k(array, k):
    left = 0
    right = len(array)-1
    while(left < right):
        if sum(array[left:right]) == k:
            return len(array[left:right])
        elif array[left] > array[right]:
            left += 1
        elif array[right] > array[left]:
            right -= 1
    return -1
        
array = [2, 3, 5]
k = 5

# array = [ 10, 5, 2, 7, 1, 9 ]
# k = 15

# array = [-5, 8, -14, 2, 4, 12]
# k = -5

# k = 10
# array = [2,3,5,1,9]
print("output ::: ",get_largest_subarray_of_sum_k(array, k))


# Question Ref:
# https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/
# https://www.geeksforgeeks.org/longest-sub-array-sum-k/

