# program for Decimal to Binary conversion
def Decimal_to_Binary(num):
    if num//2==0:
        return num
    return str(Decimal_to_Binary(num//2)) + str(num%2)
print(Decimal_to_Binary(3))