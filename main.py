"""
Example 1:
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

Example 2:
Input: prices = {1, 0, 1, 1, 0, 1} 
Output: 2
Explanation: There are two consecutive 1's in the array. 
            
Ref :
https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array

"""

def maxConsecutiveOnes(l):
    maxvalue=0
    count=0
    for i in range(len(l)):
        if l[i]==1:
            count=count+1
            maxvalue=max(count, maxvalue)
        else:
            count=0
    return maxvalue

l = [1,2,3,3,1,1,1,2,1,2]
print(maxConsecutiveOnes(l))
