rows = 4

for i in range(rows):
    for _ in range(rows-i-1):
        print(" ",end="")
    for j in range(rows):
        if i==0 or i==rows-1 or j == 0 or j == rows-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
