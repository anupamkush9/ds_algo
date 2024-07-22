# def draw_diamond(n):
#     # for uppper 1st half
#     for i in range(n):
#         for space in range(n-i-1):
#             print(" ",end="")
#         for j in range(i+1):
#             print("*", end=" ")
#         print()

#     # for lower 2nd half
#     for i in range(n-2,-1,-1):
#         for space in range(n-i-1):
#             print(" ",end="")
#         for j in range(i+1):
#             print("*", end=" ")
#         print()            
            

# n = int(input("Enter no of rows "))
# draw_diamond(n)



def print_diamond(n):
    # Upper part of the diamond
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    # Lower part of the diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Example usage:
n = 5
print_diamond(n)





# def print_pattern(rows):
#     # Upper part of the pattern
#     for i in range(1, rows + 1):
#         print(' ' * (rows - i) + '* ' * i)
    
#     # Lower part of the pattern
#     for i in range(rows - 1, 0, -1):
#         print(' ' * (rows - i) + '* ' * i)

# # Number of rows for the upper part
# rows = 4
# print_pattern(rows)
