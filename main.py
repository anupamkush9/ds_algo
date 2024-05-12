class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data, next=None):
        new_node = Node(data, next)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  
        
    def printll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            while current:
                print(f"{current.data}-->", end=" ")
                current = current.next
            print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(20)
ll.insert(20)
ll.insert(30)
ll.printll()

