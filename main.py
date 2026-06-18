"""
Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.


Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
"""

def get_single_element(l):
    ans = 0
    for ele in l:
        ans ^= ele
    return ans

l = [4,1,2,1,2]
print("ans::::", get_single_element(l))


# Question Ref :
# https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/
