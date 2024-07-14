# Question1:
# Find the length of string

def find_the_length_of_string(s):
    if s == "":
        return 0
    else:
        return 1 + find_the_length_of_string(s[1:])
print(find_the_length_of_string("aa123"))