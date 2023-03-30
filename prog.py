class Node():
    def __init__(self, value):
        self.value = value,
        self.next = None

class SlinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

slinkedlist_obj = SlinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

slinkedlist_obj.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
slinkedlist_obj.tail = n4

