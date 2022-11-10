# power of number
def power(num, pow):
    if pow==1:
        return num
    pow -= 1
    return num * power(num, pow)

print(power(2,3))