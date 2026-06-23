"""
Input: arr = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 is -1, since it does not exist.

Input : arr = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation : In the array, the next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on the right and hence -1.

Ref:
https://takeuforward.org/data-structure/next-greater-element-using-stack
"""

# Brute force approach
def nex_greater(l):
    next_greater_element = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] < l[j]:
                next_greater_element.append(l[j])
                break
        else:
            next_greater_element.append(-1)
    return next_greater_element


# using stack optimized approach

# l = [50, 40, 30, 10]
# print(nex_greater(l))

# ref : https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1
# brute force apporach



# Solution class to find next greater elements
class Solution:
    # Function to find next greater elements
    def nextGreater(self, nums):
        # Stack to store elements
        stack = []

        # Result array of same size
        n = len(nums)
        res = [0] * n

        # Traverse from right to left
        for i in range(n - 1, -1, -1):

            # Pop all smaller or equal elements
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            # If stack is empty, no greater element
            if not stack:
                res[i] = -1

            # Else top of stack is the answer
            else:
                res[i] = stack[-1]

            # Push current element
            stack.append(nums[i])

        # Return the result
        return res

# Main function
def main():
    nums = [4, 5, 2, 10]
    sol = Solution()
    ans = sol.nextGreater(nums)
    print(" ".join(map(str, ans)))

main()
