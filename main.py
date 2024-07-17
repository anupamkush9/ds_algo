class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def inset_at_begining(self, data, next = None):
        new_node = Node(data, next)
        new_node.next = self.head
        self.head = new_node

    def remove_first_element(self):
        self.head = self.head.next
        
    def remove_last_element(self):
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def length_of_linked_list(self):
        count = 0
        current = self.head
        while current:
            count = count + 1
            current = current.next
        return count
        
    def inset_at_specific_index(self, index, data, next=None):
        if index == 0:
            return 
        new_node = Node(data, next)
        count = 0
        current = self.head
        while current.next:
            if count == index-1:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
            count = count + 1

    def insert(self, data, next=None):
        new_node = Node(data, next)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  
    
    def search_element(self, target):
        current = self.head
        index = -1
        while current.data:
            index += 1  
            if current.data == target:
                return index
            current = current.next
        return index
            
            
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
ll.inset_at_begining(0)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.inset_at_specific_index(1, 60)
ll.remove_first_element()
ll.remove_last_element()
print(f"element is available at {ll.search_element(30)} index")
ll.printll()
print(f"lenght of linked_list is : ",ll.length_of_linked_list())

