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
