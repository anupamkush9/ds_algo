def print_num(n):
    if n==0:
        return 1
    else:
        # print(n)        # for printing number from 1 to 5
        print_num(n-1)
        print(n)        # for printing number from 5 to 1
print_num(5)