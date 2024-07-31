cols, rows = map(int, input("Enter no of cols and rows separated by space: ").split())
arr = [[0 for _ in range(cols)] for _ in range(rows)]

print("Enter elements of the matrix:")
for i in range(rows):
    for j in range(cols):
        arr[i][j] = int(input())


print("sum of diagonal elements")
sum = 0
for i in range(rows):
    for j in range(cols):
        if i == j:
            sum += arr[i][j]
            
print("Entered Array is : ", arr)
print("sum:::",sum)