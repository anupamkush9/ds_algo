"""
Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.

Ref :
https://www.geeksforgeeks.org/dsa/kth-smallest-largest-element-in-unsorted-array/

"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

def get_kth_smallest(arr, k):
    sorted_arr = quicksort(arr)
    return sorted_arr[k - 1]  # k is 1-based index

arr = [3, 6, 8, 10, 1, 2, 1]
print(get_kth_smallest(arr, 4))  # 3
