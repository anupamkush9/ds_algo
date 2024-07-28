
# def get_intersection_elements(A, B):
#     """
#         By Brute force, Approach implementation
#     """
#     intersection_elements = []
#     for ele in A:
#         if ele in B:
#             intersection_elements.append(ele)
#     return intersection_elements


def get_intersection_elements(A, B):
    left = 0
    right =0
    left_len = len(A)-1
    right_len = len(B)-1
    intersection_elements = []
    while left < left_len or right < right_len:
        if A[left] == B[right]:
            intersection_elements.append(A[left])
            left += 1
            right += 1
        elif  A[left] > B[right]:
            right += 1
        else:
            left += 1
    return intersection_elements

# A = [1, 2, 3, 3, 4, 5, 6]
# B = [3, 3, 5]

A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 5]
print("intersection_elements: ",get_intersection_elements(A, B))

# Question Ref : 
# https://takeuforward.org/data-structure/intersection-of-two-sorted-arrays/