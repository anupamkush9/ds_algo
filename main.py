"""
Input: a = [4, 1, 2], b = [2, 4, 1]
Output: 0
Explanation: If we take the pairings as (4,4), (1,1), and (2,2), 
the sum will be S = |4 - 4| + |1 - 1| +|2 - 2| = 0.
It can be shown that this is the minimum sum we can get.

Input: a = [4, 1, 8, 7], b = [2, 3, 6, 5]
Output: 6
Explanation:If we take the pairings as (1,2), (4,3), (7,5), and (8,6), 
the sum will be S = |1 - 2| + |4 - 3| + |7 - 5| + |8 - 6| = 6.
It can be shown that this is the minimum sum we can get.
"""

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
