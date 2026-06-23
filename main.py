"""
Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6]
Explanation: 
1st contiguous subarray [1, 2, 3], max = 3
2nd contiguous subarray [2, 3, 1], max = 3
3rd contiguous subarray [3, 1, 4], max = 4
4th contiguous subarray [1, 4, 5], max = 5
5th contiguous subarray [4, 5, 2], max = 5
6th contiguous subarray [5, 2, 3], max = 5
7th contiguous subarray [2, 3, 6], max = 6


Input: arr[] = [5, 1, 3, 4, 2], k = 1
Output: [5, 1, 3, 4, 2]
Explanation: When k = 1, each element in the array is its own subarray, so the output is simply the same array

"""

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

