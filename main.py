def get_single_element(l):
    ans = 0
    for ele in l:
        ans ^= ele
    return ans

l = [4,1,2,1,2]
print("ans::::", get_single_element(l))


# Question Ref :
# https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/