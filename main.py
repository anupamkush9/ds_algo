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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left   = [x for x in arr if x < pivot]   # Less than pivot
    middle = [x for x in arr if x == pivot]  # Equal to pivot (all duplicates)
    right  = [x for x in arr if x > pivot]   # Greater than pivot
    
    return quick_sort(left) + middle + quick_sort(right)

arr = [1, 7, 4, 1, 10, 9, -2]
arr = quick_sort(arr)
print(arr)  # [-2, 1, 1, 4, 7, 9, 10]
