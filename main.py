# largest subarray of sum k by sliding window

def maximum_of_all_subarray(array, k):
    ans = []
    for i in range(len(array)-k+1):
        ans.append(max(array[:i+k]))
    return ans
        

k = 3
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
# Output: 
# 3 3 4 5 5 5 6 


# k = 4
# arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
# Output: 
# 10 10 10 15 15 90 90
print("output ::: ",*maximum_of_all_subarray(arr, k))


# Question Ref:
# https://takeuforward.org/data-structure/sliding-window-maximum/f
# https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1

