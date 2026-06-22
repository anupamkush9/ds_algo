"""
Input: s="geeksforgeeks"
Output: 'e'
Explanation: 'e' occurs 4 times in the string

Input: s="test"
Output: 't'
Explanation: 't' occurs 2 times in the string

Ref:
https://www.geeksforgeeks.org/dsa/return-maximum-occurring-character-in-the-input-string-3/
"""


def get_max_occurance_of_character(input_str):
    char_count_mapping = {}

    for char in input_str:
        if char in char_count_mapping.keys():
            char_count_mapping[char] = char_count_mapping.get(char) + 1
        else:
            char_count_mapping[char] = 1
    max_key = max(char_count_mapping, key=char_count_mapping.get)
    return max_key, char_count_mapping[max_key]
    
s = "aaabbbcccccaaa"
print("get_max_occurance_of_consecutive_character:::::>>>",get_max_occurance_of_character(s))