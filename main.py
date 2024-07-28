from collections import Counter

def top_k_frequent_elements(nums, k):
    counter = Counter(nums)
    sorted_element_by_frequency = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))
    return [ele for ele,freq in sorted_element_by_frequency[:k]]

N = 8
nums = [1, 1, 2, 2, 3, 3, 3, 4]
k = 2
print(top_k_frequent_elements(nums, k))


# Ref : https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1