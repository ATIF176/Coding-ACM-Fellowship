class MyQueue(object):

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        self.queue.append(x)
        

    def pop(self):
        return self.queue.pop(0)
        

    def peek(self):
        return self.queue[0]
        

    def empty(self):
        if self.queue == []:
            return True
        else:
            return False
        

# Test Case 1
obj = MyQueue()

obj.push(1)
obj.push(2)
obj.push(3)


param_2 = obj.pop()
print(param_2)

param_3 = obj.peek()
print(param_3)