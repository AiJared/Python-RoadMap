# Stack Data Structure
class Stack:
    def __init__(self, item):
        self.item = []
    
    # Push items on top of the stack
    def add_item(self):
        return self.item.append()
    
    # Method to remove item ontop of the stack
    def remove_item(self):
        if not self.is_empty:
            return self.item.pop()
        else:
            return f"Stack is empty!"
    