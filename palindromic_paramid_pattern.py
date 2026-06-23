"""
Input : Enter the row 5
Output :
    1
   121
  12321
 1234321
123454321

"""

n = 5

for i in range(1, n+1):
    for _ in range(n-i):
        print(" ",end="")
    for k in range(1, i):
        print(k,end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print("")
