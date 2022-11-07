def fibonacci(a, b, n):
    if n==1:
        return a + b
    print(a + b)
    return fibonacci(b, a+b, n-1)

print(0)
print(1)
print(fibonacci(0,1,5))