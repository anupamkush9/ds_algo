"""
Input: N = 5, Arr[] = {4,1,7,9,3}
Output: {1, 3, 4, 7, 9}
Explanation: After sorting the array in ascending order it becomes 1, 3, 4, 7, 9

Input: N = 8, Arr[] = {4,6,2,5,7,9,1,3}
Output: {1, 2, 3, 4, 5, 6, 7, 9}
Explanation: After sorting the array in ascending order it becomes 1, 2, 3, 4, 5, 6, 7, 9

Ref:
https://www.geeksforgeeks.org/dsa/python-program-for-quicksort/
https://youtu.be/8MNB0Mba_Dc?si=NrMYiWApTuTA5Tw4
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

# Example
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # [1, 1, 2, 3, 6, 8, 10]