"""

Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.


Example 2:
Input Format: N = 3, array[] = {1,3}
Result: 2
Explanation: In the given array, number 2 is missing. So, 2 is the answer.

Ref :
https://takeuforward.org/data-structure/check-if-two-strings-are-anagrams-of-each-other
https://www.geeksforgeeks.org/dsa/check-whether-two-strings-are-anagram-of-each-other/

"""


# def find_missing_number(nums):
#     for i in range(len(nums)-1):
#         if nums[i+1] - nums[i] != 1:
#             return nums[i] + 1

# nums = [1,2,3,4,6,7,8,9,10,11]
# print("missing number is : ",find_missing_number(nums))
    
class Solution:
    def missingNumber(self, a, N):
        total_sum = (N * (N + 1)) // 2
        actual_sum = sum(a)
        return total_sum - actual_sum

# Driver code
a = [1, 2, 4, 5]
N = 5
obj = Solution()
ans = obj.missingNumber(a, N)
print("The missing number is:", ans)
