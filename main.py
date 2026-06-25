
"""
# ============================================================
# Previous Smaller Element / Nearest Smaller Element on Left
# ============================================================

# Problem:
# For every element in array, find nearest smaller element on left.
# If not found, return -1.

# Example:
# arr = [1, 5, 0, 3, 4, 5]
# output = [-1, 1, -1, 0, 3, 4]

Input: arr[] = [1, 6, 2]
Output: [-1, 1, 1]

# https://www.geeksforgeeks.org/dsa/find-the-nearest-smaller-numbers-on-left-side-in-an-array/

"""
def prevSmaller_bruteforce(arr):
    n = len(arr)
    result = [-1] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                result[i] = arr[j]
                break

    return result


def prevSmaller_stack(arr):
    result = []
    stack = []

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        stack.append(num)

    return result


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
arr = [1, 5, 0, 3, 4, 5]

print("Brute Force :", prevSmaller_bruteforce(arr))
print("Stack       :", prevSmaller_stack(arr))