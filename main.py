
def reverse_queue(l):
    reversed_queue = []
    for ele in l[::-1]:
        reversed_queue.append(ele)
    return reversed_queue

l = [1,2,3,4]
print(reverse_queue(l))
