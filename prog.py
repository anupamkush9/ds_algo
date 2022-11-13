def power_of_3(n):
    if (n == 1):
        return True
    if (n % 3 != 0):
        return False
    if (n < 3):
        return False
    return power_of_3(n // 3)

print(power_of_3(81))