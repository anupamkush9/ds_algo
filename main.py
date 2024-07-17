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
        print("-->",current.data)
        
    def reversell(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.reversell()
ll.printll()

    

# Ref : https://www.geeksforgeeks.org/reverse-a-linked-list/