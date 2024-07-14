# Question1:
#     For a given integer array of sizeN.You have to find all the occurrences (indices) of a given element (Key)
#     and print them. Use a recursive function to solve this problem.
#     Sample Input: arr[ ] = {3, 2, 4, 5, 6, 2, 7, 2, 2}, key = 2
#     Sample Output: 1 5 7 8


def element_indexes(l, indexes, target, results):
    if indexes == len(l) -1:
        if l[indexes] == target:
            results.append(indexes)
            return results
    if indexes < len(l)-1:
        if l[indexes] == target:
            results.append(indexes) 
            idx = indexes+1
            return element_indexes(l, idx, target, results)
        idx = indexes+1
        return element_indexes(l, idx, target, results)

print(element_indexes([3, 2, 4, 5, 6, 2, 7, 2, 2], 0, 2, []))