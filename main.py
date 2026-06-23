"""
Example 1:
Input:
 S = "abcddabac"  
Output:
 4  
Explanation:
 The longest substring with distinct characters is "abcd", which has a length of 4.

Example 2:
Input:
 S = "aaabbbccc"  
Output:
 2  
Explanation:
 The longest substrings with distinct characters are "ab" and "bc", both having a length of 2.
 
Ref : https://takeuforward.org/data-structure/length-of-longest-substring-without-any-repeating-character 
"""

def calc_longest_substring(input_str):
    max_length_sub_str = 0
    unique_array = []
    for char in input_str:
        if char not in unique_array:
            unique_array.append(char)
            unique_array_length = len(unique_array)
            if max_length_sub_str <= unique_array_length:
                max_length_sub_str = unique_array_length
        else:
            unique_array = [char]
    return max_length_sub_str


input_str = "abcabcbaa"
print("------>", calc_longest_substring(input_str))