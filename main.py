def nex_greater(l):
    next_greater_element = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] < l[j]:
                next_greater_element.append(l[j])
                break
        else:
            next_greater_element.append(-1)
    return next_greater_element
        
l = [50, 40, 30, 10]
print(nex_greater(l))

# ref : https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1
# brute force apporach