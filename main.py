def linear_search(a, target):
    for index, element in enumerate(a):
        if element == target:
            return index
    else:
        return -1

a = [10,5,55,2,54]
target = 54
print(linear_search(a, target))