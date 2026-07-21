"""
Input: s = "geeksforgeeks"
Output: 'f'
Explanation: 'f' is the first character in the string which does not repeat.

Input: s = "racecar"
Output: 'e'
Explanation: 'e' is the only character in the string which does not repeat.

Input: "aabbccc"
Output: '$'
Explanation: All the characters in the given string are repeating.

Ref :
https://www.geeksforgeeks.org/dsa/given-a-string-find-its-first-non-repeating-character/
"""

# Time Complexity: O(n)
# Space Complexity: O(n)
def first_non_repeating_char(s):
    char_count = {}

    # Count frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first character with frequency 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

string = "aabbcdde"
result = first_non_repeating_char(string)

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")


# Time Complexity: O(n²)
# def first_non_repeating_char(s):
#     for char in s:
#         if s.count(char) == 1:
#             return char
#     return None

# print(first_non_repeating_char("aabbcdde"))
