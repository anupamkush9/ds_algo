"""
Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
Output: [4, 1]
Explanation: Frequency of 4 is 2 and frequency of 1 is 2, these two have the maximum frequency and 4 is larger than 1.

Input: arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
Output: [5, 11, 7, 10]
Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, frequency of 10 is 1.
"""

from collections import Counter

# def top_k_frequent_elements(nums, k):
#     counter = Counter(nums)
#     sorted_element_by_frequency = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))
#     return [ele for ele,freq in sorted_element_by_frequency[:k]]

def top_k_frequent_elements(nums,k):
    count_dict = {}
    for item in nums:
        if item not in count_dict.keys():
            count_dict[item] = 1
        else:
            count_dict[item] = count_dict[item] + 1
    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_dict.keys())[:k]

N = 8
nums = [1, 1, 2, 2, 3, 3, 3, 4]
k = 2
print(top_k_frequent_elements(nums, k))


# Ref : https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1
