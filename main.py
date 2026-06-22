"""

input_str = "aaabbbbcccccaaa"
c = 5
"""
def get_max_occurance_of_consecutive_character(input_str):
    max_count = 1
    max_character = input_str[0]
    current_count = 1
    prev_char = input_str[0]
    
    for current_char in input_str[1:]:
        if current_char == prev_char:
            current_count = current_count + 1
            if max_count < current_count:
                max_count = current_count
                max_character = current_char
        else:
            prev_char = current_char
            current_count = 1
    return max_character, max_count
        
    
input_str = "aaabbbbcccccaaa"
print(get_max_occurance_of_consecutive_character(input_str))

# Ref : https://www.geeksforgeeks.org/maximum-consecutive-repeating-character-string/
