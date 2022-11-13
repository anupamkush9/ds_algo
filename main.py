# def power_of_two(n):
#     if (n==1):
#         return True
#     if (n%2 != 0):
#         return False
#     return power_of_two(n//2)
# print(power_of_two(16))

def power_of_two(n):
    if(n & (n-1) == 0):
        return True
    else:
        return False
print(power_of_two(16))