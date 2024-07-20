class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def print_all_queue_elements(self):
        print("below are the elements of queue")
        for ele in self.stack1[::-1]:
            print(ele, end="-")
        print()

    def enqueue(self, item):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(item)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if not self.stack1:
            raise IndexError("dequeue from empty queue")
        return self.stack1.pop()

    def is_empty(self):
        return not self.stack1

    def size(self):
        return len(self.stack1)

    def peek(self):
        if not self.stack1:
            raise IndexError("peek from empty queue")
        return self.stack1[-1]

queue = QueueUsingTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_all_queue_elements()
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
queue.enqueue(4)
queue.print_all_queue_elements()
print(queue.dequeue())  # Output: 3
print(queue.peek())     # Output: 4
print(queue.dequeue())  # Output: 4
queue.print_all_queue_elements()
print(queue.is_empty())
print(queue.size())

# https://medium.com/@chauhanvaibhav1105/queue-implementation-using-two-stacks-3fce01fe5463
