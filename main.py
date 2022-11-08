
def length_by_recursion(s):
    if len(s) == 1:
        return 1
    return 1 + length_by_recursion(s[:-1])

s = input()
print(length_by_recursion(s))

