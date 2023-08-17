# Initialize Queue Class
class MyQueue:

    def __init__(self):
        self.queue = []

    # Check if Queue is Empty
    def isEmpty(self):
        if self.queue == []:
            return True
        else:
            return False

    # EnQueue an element in Queue
    def enqueue(self, item):
        self.queue.append(item)
        return str(item) + " Enqueued."
    

    # DeQueue an element from Queue
    def DeQueue(self):
        if self.queue:
            self.queue.pop(0)
            return str(self.queue.pop(0)) + " Dequeued."
        

    # Display  the queue
    def display(self):
        for i in range(len(self.queue)):
            print(self.queue[i], end=" ")
    
    # Get the size of the queue
    def size(self):
        return "Size of queue is" + str(len(self.queue))
    
    # Get the front element of the queue
    def front(self):
        return "Front element is " + str(self.queue[0])
    

    # Get the rear element of the queue
    def rear(self):
        return "Rear element is " + str(self.queue[-1])
    

    # Search for an element in the queue
    def search(self, item):
        for i in range(len(self.queue)):
            if self.queue:
                if self.queue[i] == item:
                   return True
            else:
                return "Queue is empty"
        return False
            

# Initialize a Queue Object
queue = MyQueue()

# EnQueue 5 elements
print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print(queue.enqueue(4))
print(queue.enqueue(5))

# Display the queue
print("Queue: ")
queue.display()

# DeQueue 2 elements
print("\n\nDeQueue 2 elements")
print(queue.DeQueue())
print(queue.DeQueue())

# Display the queue
print("\nQueue: ")
queue.display()

# Get the size of the queue
print("\n\n" + queue.size())

# Get the front element of the queue
print("\n" + queue.front())

# Get the rear element of the queue
print("\n" + queue.rear())

# Search for an element in the queue
print("\nSearch for 3 in the queue")
print(queue.search(3))


