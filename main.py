def get_missing_number_by_hashing(l):
    length_Of_arr = len(l) + 2
    hash_arr = [0]*length_Of_arr
    for i in l:
        hash_arr[i] = 1
    for i in range(1, len(hash_arr)):
        if hash_arr[i] == 0:
            return i

def get_missing_number_by_sum_of_n_natural_number(l):
    max_element = max(l)
    sum_of_n_natural_number = (max_element*(max_element+1))//2
    sum_of_list = sum(l)
    return sum_of_n_natural_number - sum_of_list

def get_missing_number_by_xor_operator(l):
    max_element = max(l)+1
    ans = 0
    for i in range(max_element):
        ans ^= i
    for ele in l:
        ans ^= ele
    return ans

l = [1, 2, 4, 5]
# print("ans::::", get_missing_number_by_hashing(l))
# print("ans::::", get_missing_number_by_sum_of_n_natural_number(l))
print("ans::::", get_missing_number_by_xor_operator(l))


# Question Ref :
# https://takeuforward.org/arrays/find-the-missing-number-in-an-array/
