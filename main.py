"""

Input: N = 5, arr[] = {2,6,5,8,11}, target = 14
Output : YES
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for first variant for second variant output will be : [1,3].

Input: N = 5, arr[] = {2,6,5,8,11}, target = 15
Output : NO.
Explanation: There exist no such two numbers whose sum is equal to the target. 

Ref : https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array
https://interviewing.io/questions/two-sum
"""


class SolutionBruteForce:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class SolutionTwoPointers:
    def twoSum(self, nums, target):
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()

        left, right = 0, len(arr) - 1

        while left < right:
            curr_sum = arr[left][0] + arr[right][0]

            if curr_sum == target:
                return [arr[left][1], arr[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return []


class SolutionHashMap:
    def twoSum(self, nums, target):
        num_to_index = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[nums[i]] = i

        return []


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
nums = [2, 7, 11, 15]
target = 9

print("Approach 1:", SolutionBruteForce().twoSum(nums, target))
print("Approach 2:", SolutionTwoPointers().twoSum(nums, target))
print("Approach 3:", SolutionHashMap().twoSum(nums, target))