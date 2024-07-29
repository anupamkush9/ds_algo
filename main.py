# largest subarray of sum k by sliding window

def longest_substring_with_k_unique_characters(array, k):
    dict = {}
    max_len = 0
    arr_len = len(array)
    left, right = 0, 0
    while right < arr_len:
        dict[array[right]] = dict.get(array[right], 0)+1
        if len(dict.keys()) == k:
            max_len = sum([val for key,val in dict.items()])
        while len(dict.keys()) > k:
            if array[left] in dict.keys():
                del dict[array[left]]
            left += 1
        right += 1  
    return max_len
        
arr = "aabbcc"
k = 1
# Output: 2
# Explanation: Max substring can be any one from {“aa” , “bb” , “cc”}.

# arr = "aabbcc"
# k = 2
# Output: 4
# Explanation: Max substring can be any one from {“aabb” , “bbcc”}.
# arr = "aabbcc"
# k = 3
# Output: 6
print("------>",longest_substring_with_k_unique_characters(arr, k))
# Question Ref:
# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/

# https://www.youtube.com/watch?v=Lav6St0W_pQ&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=10
# Above video title -->>  Longest Substring With K Unique Characters | Variable Size Sliding Window