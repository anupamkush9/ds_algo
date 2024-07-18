def minAbsoluteDiff(a, b, n):
    a.sort()
    b.sort()
    abs_min_diff = 0
    for a_ele,b_ele in zip(a,b):
        abs_min_diff += abs(a_ele-b_ele)
    return abs_min_diff
    
    
# a = [4, 1, 8, 7]
# b = [2, 3, 6, 5]
a = [4, 1, 8]
b = [2, 3, 6]
n = len(a)
print(minAbsoluteDiff(a, b, n))


# Ref : https://www.geeksforgeeks.org/minimum-sum-absolute-difference-pairs-two-arrays/