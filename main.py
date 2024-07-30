# Python3 program to find N'th node from end
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def nth_from_end(self, n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        while count < n:
            if ref_ptr is None:
                return -1
            ref_ptr = ref_ptr.next
            count += 1
        
        while ref_ptr is not None:
            ref_ptr = ref_ptr.next
            main_ptr = main_ptr.next
        
        return main_ptr.data
    
# Driver code
ll = LinkedList()

ll.insert_at_begin(20)
ll.insert_at_begin(4)
ll.insert_at_begin(15)
ll.insert_at_begin(35)

# Function call
print(ll.nth_from_end(4))


# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/