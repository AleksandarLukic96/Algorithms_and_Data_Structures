# Aleksandar Lukic 

# This is and implementation of a static stack using size defined arrays

# A stack is a dynamic sequence, which supports the operations push(x) and pop()
# Think of a stack of books on a table. In order to get a specific book,
# you would have to remove every book on top of it to reach it.
# This is the idea of the stack data structure.

class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
    
    # Function to print stack:
    def print(self):
        print(self.stack)
    
    # Function to check if stack is empty
    def isEmpty(self):
        if(self.top == -1):
            return True
        return False
    
    # Function to check if stack is full
    def isFull(self):
        if(self.top == len(self.stack)-1):
            return True
        return False
    
    # Function to push element after top
    def push(self, element):
        if(self.isFull() != True):
            self.top += 1
            self.stack[self.top] = element
    
    # Function to pop element from top
    def pop(self):
        if (self.isEmpty() != True):
            self.top -= 1
            popped = self.stack[self.top + 1]
            self.stack[self.top + 1] = None
            return popped 

if __name__ == "__main__":
    # Testbench
    stack = Stack(3)
    print("Current stack:")
    stack.print()
    stack.push("Anna Karenina")
    print("Current stack:")
    stack.print()
    stack.push("Great Expectations")
    print("Current stack:")
    stack.print()
    stack.push("Wuthering Heights")
    print("Current stack:")
    stack.print()
    stack.push("Queen")
    print("Popped from stack: " + str(stack.pop()))
    print("Popped from stack: " + str(stack.pop()))
    print("Current stack:")
    stack.print()
    print("Popped from stack: " + str(stack.pop()))
    print("Popped from stack: " + str(stack.pop()))
    print("Current stack:")
    stack.print()
        