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
        
    def reverse_ll_by_stack(self):
        current = self.head
        stack = []
        while current:
            stack.append(current.data)
            current = current.next
        current = self.head
        while current:
            current.data = stack.pop()
            current = current.next
        

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
print("===Before reversal=======++>")
ll.printll()
ll.reverse_ll_by_stack()
print("\n===After reversal=======++>")
ll.printll()

    

# Ref : https://takeuforward.org/data-structure/reverse-a-linked-list/
        # brute force approach implemented