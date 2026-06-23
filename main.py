"""
Example 1:
nums = [2, 3, 5, -2, 7, -4]  
Output: 15  
Explanation: The subarray from index 0 to index 4 has the largest sum = 15, which is the maximum sum of any contiguous subarray.

Example 2:
nums = [-2, -3, -7, -2, -10, -4]  
Output: -2  
Explanation: The largest sum is -2, which comes from taking the element at index 0 or index 3 as the subarray. Since all numbers are negative, the subarray with the least negative number gives the largest sum.

Ref :
https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array

"""

# Brute force approach
def maxSubArray(nums):
    maxi = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > maxi:
                maxi = current_sum
    return maxi

# optimized approach using Kadane's algorithm
def maxSubArray(nums): 
    maxi = nums[0]
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum > maxi:
            maxi = current_sum
        if current_sum < 0:
            current_sum = 0
    return maxi

def maxSubArray(nums):
    cur = max_sum = nums[0]
    for i in range(1, len(nums)):
        cur = max(nums[i], cur + nums[i])   # extend or restart
        max_sum = max(max_sum, cur)

    return max_sum

numbers = [2, 3, 5, -2, 7, -4] 
print(maxSubArray(numbers))  # Output: 15
