# program for GCD ( Greatest Common Divisor )
def GCD(num1, num2):
    if num1 > num2:
        if num1 % num2 != 0:
            return GCD(num2, (num1%num2))
        else:
            return num2
    else:
        if num2 % num1 != 0:
            return GCD(num1, (num2%num1))
        else:
            return num1

print(GCD(10,35))