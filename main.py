class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            
        
    def printll(self):
        current = self.head
        while current.next:
            print("-->",current.data, end='')
            current = current.next
        print("-->",current.data, end='')
        
    def findMid(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def check_is_palindrome(self):
        midNode = self.findMid()
        prev = None
        
        # reversing half ll
        while midNode:
            temp_next = midNode.next
            midNode.next = prev
            prev = midNode
            midNode = temp_next
        
        # comparing 1st half ll by 2nd half ll
        left = self.head
        right = prev
        while right.next:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True

        

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(20)
ll.insert(10)
ll.insert(10)
print(ll.check_is_palindrome())


    

# Ref : https://takeuforward.org/data-structure/check-if-given-linked-list-is-plaindrome/
        # Optimal approach implementation