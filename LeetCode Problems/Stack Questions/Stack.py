# Create Stack class
class Stack:
    def __init__(self):
        self.items = []
    
    # Check if the stack is empty
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    
    # Add element to the stack
    def AddElement(self, item):
        self.items.append(item)
        return str(item) + " is added."
    

    # Remove element from the stack
    def RemoveElemnt(self):
        return str(self.items.pop()) + " is popped."
    

    # Get the size of the stack
    def size(self):
        return "Size of Stack is " + str(len(self.items))
    

    # Get the top element of the stack
    def peek(self):
        return "Top Element of Stack is " + str(self.items[len(self.items)-1])
    

    # Search your desire element
    def Search(self, num):
        for i in range(0,len(self.items)):
            if self.items:
                if self.items[i] == num:
                    return "Found"
        return "Not Found"
    

# Test the Stack class
my_stack = Stack()

# Add elements to the stack
print(my_stack.AddElement(1))
print(my_stack.AddElement(2))
print(my_stack.AddElement(3))

# Remove elements from the stack
print(my_stack.RemoveElemnt())

# Get the size of the stack
print(my_stack.size())

# Get the top element of the stack
print(my_stack.peek())

# Check if the stack is empty
print(my_stack.isEmpty())

# Search your desire element
print(my_stack.Search(3))