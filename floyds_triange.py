rows = 5
count = 1
for row in range(rows):
    for i in range(row+1):
        print(count, end=" ")
        count += 1
    print()
