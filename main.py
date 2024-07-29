# count occurances of anagram by sliding window

def get_anagram_string_count(s, anagram_string):
    count = 0
    anagram_string_sorted = ''.join(sorted(anagram_string))
    for i in range(len(s)-len(anagram_string)+1):
        window_str_sorted = ''.join(sorted(s[i:i+len(anagram_string)]))
        if window_str_sorted == anagram_string_sorted:
            count += 1
    return count

s = "forxxorfxdofr"
anagram_string = "for"

# s = "aabaabaa"
# anagram_string = "aaba"
print("output ::: ",get_anagram_string_count(s, anagram_string))


# Question Ref:
# https://www.geeksforgeeks.org/count-occurrences-of-anagrams/