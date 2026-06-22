"""
Input : lst =[1, 5, 3, 7, 9]
        K = 12
Output : [(5, 7), (3, 9)]


int_array = [2,3,5,7,8,9]
Output : [(2, 8), (3, 7)]

Ref:
https://www.geeksforgeeks.org/python/python-program-to-find-all-possible-pairs-with-given-sum/

"""


def calculate_sum_of_array(int_array, target_sum):
    left = 0
    right = len(int_array)-1
    correct_pairs = []
    while left < right:
        if ((int_array[left]+int_array[right]) == target_sum):
            correct_pairs.append((int_array[left], int_array[right]))
            left = left+1
            right = right-1
        elif (int_array[left]+int_array[right]) > target_sum:
            right = right-1
        else:
            left = left + 1
    return correct_pairs

int_array = [2,3,5,7,8,9]
target = int(input("Please enter target value\n"))
print("sum of pairs are : ", calculate_sum_of_array(int_array, target))

