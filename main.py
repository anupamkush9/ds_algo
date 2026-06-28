"""

Input: arr[] = [10, 2, 3, 4, 5, 7, 8], target = 23 
Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]] 
Explanation: There are only three distinct quadruplets with sum = 23.


Input Format: arr[] = [4,3,3,4,4,2,1,2,1,1], target = 9
Result: [[1,1,3,4],[1,2,2,4],[1,2,3,3]]
Explanation: The sum of all the quadruplets is equal to the target i.e. 9.


Ref:
https://takeuforward.org/data-structure/4-sum-find-quads-that-add-up-to-a-target-value
https://www.geeksforgeeks.org/dsa/find-four-elements-that-sum-to-a-given-value-set-2/

"""

class Solution:
    # Function to find all unique quadruplets
    def fourSum(self, arr, target):
        n = len(arr)
        arr.sort()
        ans = []

        # Step 1: First loop for first number
        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Step 2: Second loop for second number
            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                # Step 3: Two pointers
                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == target:
                        ans.append([arr[i], arr[j], arr[left], arr[right]])

                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return ans


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
print(obj.fourSum(arr, target))
