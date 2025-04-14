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
