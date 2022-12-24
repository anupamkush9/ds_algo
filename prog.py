from array import *

arr = array('i', [1, 2, 3, 4, 5])

# inserting an element at the end of the array (0)1
arr.insert(len(arr),100)

# inserting an element at the start of the array (0)n
arr.insert(0,0)

# inserting an element at the middle of the array (0)n
arr.insert(len(arr)//2,55)

print("arr:::", *arr)
