n = 5

for i in range(1, n+1):
    for _ in range(n-i):
        print(" ",end="")
    for k in range(1, i):
        print(k,end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print("")