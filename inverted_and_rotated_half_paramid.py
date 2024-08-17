rows = 4
for i in range(rows):
    for _ in range(rows-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
