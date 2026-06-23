"""
Enter the number of rows: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""

rows = 5
count = 1
for row in range(rows):
    for i in range(row+1):
        print(count, end=" ")
        count += 1
    print()
