def next_greater_element(l):
    list_with_next_greater_element = [-1] * len(l)
    stack = []

    for i in range(len(l) - 1, -1, -1):
        while stack and stack[-1] <= l[i]:
            stack.pop()
        if stack:
            list_with_next_greater_element[i] = stack[-1]
        stack.append(l[i])

    return list_with_next_greater_element

# Example usage
l = [1, 3, 2, 4]
print("l:", l)
print("Next Greater Elements:", next_greater_element(l))

l = [10, 20, 30, 50]
print("l:", l)
print("Next Greater Elements:", next_greater_element(l))

# ref : https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1