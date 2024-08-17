rows = 5

for i in range(1, rows):
    for _ in range(rows-i):
        print(" ",end="")
    for j in range(i):
        print(i, end=" ")
    print()