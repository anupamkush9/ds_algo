
def palindrom(s):
    if len(s) == 1:
        return s
    return s[-1] + palindrom(s[:-1])

s = input()
if s == palindrom(s):
    print("Palindrome No")
else:
    print("Not Palindrome No")







