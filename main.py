# Input: arr[] = {1, 1, 2}
# Output: Yes
# Explanation: Removing an occurrence of 1 modifies the array to {1, 2}, which is strictly increasing array.

# Input: arr[] = {2, 2, 3, 4, 5, 5} 
# Output: No

def strictlyIncreasingArray(l):
    non_strictly_increasing_element = 0
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            non_strictly_increasing_element += 1
    return non_strictly_increasing_element == 1
            

arr = [1, 1, 2]
print("strictlyIncreasingArray===",strictlyIncreasingArray(arr))    

# Ref : https://www.geeksforgeeks.org/check-whether-an-array-can-be-made-strictly-increasing-by-removing-at-most-one-element/