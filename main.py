"""

Problem: Product of Array Except Self

Input: N = 5, array[] = {1,2,3,4,5}
Output: 120 60 40 30 24

Input:  [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]

https://www.geeksforgeeks.org/dsa/a-product-array-puzzle/
https://www.geeksforgeeks.org/dsa/a-product-array-puzzle/


"""

def method1_brute(arr):
    n = len(arr)
    res = []
    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= arr[j]
    return res


def method2_prefix_suffix(arr):
    n = len(arr)
    prefix = [1] * n
    suffix = [1] * n
    res    = [0] * n

    for i in range(1, n):
        prefix[i] = arr[i - 1] * prefix[i - 1]

    for j in range(n - 2, -1, -1):
        suffix[j] = arr[j + 1] * suffix[j + 1]

    for i in range(n):
        res[i] = prefix[i] * suffix[i]

    return res


def productArray_division(arr):

    zero_count = 0
    product = 1

    # Count zeros and multiply non-zero elements
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            product *= num

    result = []

    if zero_count > 1:
        return [0] * len(arr)

    for num in arr:

        if zero_count == 0:
            result.append(product // num)

        elif num == 0:
            result.append(product)

        else:
            result.append(0)

    return result


# Driver Code
arr = [10, 3, 5, 6, 2]
print(productArray_division(arr))

arr = [1, 2, 0, 4]
print(productArray_division(arr))

arr = [1, 0, 2, 0]
print(productArray_division(arr))
