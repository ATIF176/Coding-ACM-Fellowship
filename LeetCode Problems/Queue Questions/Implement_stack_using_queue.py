class MyStack(object):

    def __init__(self):
        self.stack =[]
        

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        return self.stack.pop()
        

    def top(self):
        return self.stack[len(self.stack)-1]
        

    def empty(self):
        if self.stack == []:
            return True
        else:
            return False
        

# Test Case 1
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)

obj.pop()


param_3 = obj.top()
print(param_3)

param_4 = obj.empty()
print(param_4)
