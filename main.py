#sum of digits of number
def sum_of_digits(num):
    if len(str(num)) == 2:
        return num//10 + num%10
    return num%10 + sum_of_digits(num//10)

s = int(input())
print(sum_of_digits(s))

