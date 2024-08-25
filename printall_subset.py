def print_subset(s, substr, level):
    if level == len(s):
        print(substr)
        return
    print_subset(s, substr + s[level], level+1)
    print_subset(s, substr, level+1)

s = "abc"
print_subset(s, "", 0)