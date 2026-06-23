"""
a program for Flattening an array
INPUT:  [1 , 2 , [3, [4,5]]];
OUTPUT:  [1,2,3,4,5]

INPUT:   [[1 , 2], [3 , 4], [5 , 6]];
OUTPUT:  [1,2,3,4,5,6]
"""


def flatten_list(arr):
    result = []

    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_list(item))   # recursive call
        else:
            result.append(item)

    return result


arr = [1, [2, [3, 4], 5], [6, 7], 8]
print(flatten_list(arr))
