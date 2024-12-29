l = [1, 2, 4, 66, 4, 2]

print("Before bubble sort ::::::::::::",l)
array_len = len(l)
for i in range(array_len):
    for j in range(array_len-i-1):
        if l[j] > l[j+1]:
            l[j+1], l[j] = l[j], l[j+1]

print("After bubble sort :::::::::::::",l)