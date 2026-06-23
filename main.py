"""
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.
Note: A subarray is a contiguous part of any given array.

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.

Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.
"""

def max_sum_subarray(nums, k):
    """
        sliding window Brute force Approach Implmentation
    """
    max_sum = 0
    for i in range(len(nums)-k+1):
        if sum(nums[i:i+k]) > max_sum:
            max_sum = sum(nums[i:i+k])
    return max_sum

def max_sum_subarray(nums, k):
    """
        Sliding window optimize Approach
    """
    max_sum = 0
    for i in range(len(nums)-k+1):
        if i == 0:
            sub_array_total = sum(nums[:k])
        else:
            sub_array_total = sub_array_total + nums[i+k-1]-nums[i-1]
        if sub_array_total > max_sum:
            max_sum = sub_array_total
    return max_sum


# nums = [100, 200, 300, 400]
# k = 2
nums = [100, 200, 300, 400]
k = 4
print(max_sum_subarray(nums, k))


# Ref : https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
