
"""
Input: arr[] = {1,2,3,4,5,6,7,8,5,1}
Output: 7
Explanation: There is only 1 peak element, 8,  that is at index 7.

https://takeuforward.org/data-structure/peak-element-in-array

"""
class SolutionB:
    def findPeakElement(self, nums):
        n = len(nums)
        ans = [-1]
        for i in range(n):

            left = float('-inf') if i == 0 else nums[i - 1]
            right = float('-inf') if i == n - 1 else nums[i + 1]

            if nums[i] > left and nums[i] > right:
                ans.append(i)
        return max(ans)

class Solution:
    def findPeakElement(self, nums):
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                # slope going down → peak is on left side (including mid)
                high = mid
            else:
                # slope going up → peak is on right side
                low = mid + 1

        # low == high → peak index
        return low



# Driver Code
nums = [1, 2, 1, 3, 5, 6, 4]
objb = SolutionB()
print(objb.findPeakElement(nums))

nums = [1, 2, 1, 3, 5, 6, 4]
obj = Solution()
print(obj.findPeakElement(nums))  # 5


