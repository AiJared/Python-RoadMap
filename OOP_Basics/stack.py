# Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []
    
    # Push items on top of the stack
    def push(self, item):
        return self.items.append(item)
    
    # Method to remove item ontop of the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"
    
    # The topmost item
    def peek(self):
        if not self.is_empty():
            return self.items[-1] # return the top item without removing it
        else:
            return "Stack is empty!"

    # Check if stack is empty
    def is_empty(self):
        return (self.items) == 0
    
    # Check the size of the stack
    def size(self):
        return len(self.items)

# Instantiate Stack object
my_stack = Stack()

# push items to the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# The topmost item in the stack
print(my_stack.peek())