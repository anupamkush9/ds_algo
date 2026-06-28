"""
Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
Output: true
Explanation: The triplet [1, 4, 8] sums up to 13

Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10 
Output: true
Explanation: The triplets [1, 3, 6] and [1, 2, 7] both sum to 10. 

Input: arr[] = [40, 20, 10, 3, 6, 7], sum = 24 
Output: false
Explanation:  No triplet in the array sums to 24.

Ref:
https://www.geeksforgeeks.org/dsa/find-a-triplet-that-sum-to-a-given-value/

"""

def hasTripletSum(arr, target):
    n = len(arr)
    arr.sort()
    
    # Fix the first element as arr[i]
    for i in range(n - 2):
        
        # Initialize left and right pointers with 
        # start and end of remaining subarray
        l = i + 1
        r = n - 1
        
        requiredSum = target - arr[i]
        while l < r:
            if arr[l] + arr[r] == requiredSum:
                return True
            if arr[l] + arr[r] < requiredSum:
                l += 1
            else:
                r -= 1
    
    return False

if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 8]
    target = 13
    if hasTripletSum(arr, target):
        print("true")
    else:
        print("false")
