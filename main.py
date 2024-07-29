def fist_negative_number_of_every_window(A, k):
    """
        By brute force approach implementation.
    """
    ans = []
    for i in range(len(A)-k+1):
        min_element_in_window = min(A[i:i+k])
        ans.append(min_element_in_window) if min_element_in_window < 0 else ans.append(0)
    return ans


A = [-8, 2, 3, -6, 10]
K = 2
print("==>>",fist_negative_number_of_every_window(A, K))
# Output : 
# -8 0 -6 -6


# https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1