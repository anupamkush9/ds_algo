"""
Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

Input: s = "aaaa", k = 2
Output: -1
Explanation: The string contains only one unique character, so there's no substring with 2 distinct characters.

Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.

"""

def longest_substring_with_k_unique_characters(array, k):
    freq = {}
    left = 0
    max_len = 0

    for right in range(len(array)):
        freq[array[right]] = freq.get(array[right], 0) + 1

        while len(freq) > k:
            freq[array[left]] -= 1
            if freq[array[left]] == 0:
                del freq[array[left]]
            left += 1

        if len(freq) == k:
            max_len = max(max_len, right - left + 1)

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
