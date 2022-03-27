# Aleksandar Lukic

# This is an implementation of a dynamic stack data structure using Singly-linked lists

# A stack is a dynamic sequence, which supports the operations push(x) and pop()
# Think of a stack of books on a table. In order to get a specific book,
# you would have to remove every book on top of it to reach it.
# This is the idea of the stack data structure.

class Node:
   def __init__(self, key = None):
      self.key = key
      self.next_node = None

class Stack:
    def __init__(self):
      self.top_node = None
    
    # Function to print stack
    def print(self):
        current_node = self.top_node
        while (current_node != None):
            print(current_node.key)
            current_node = current_node.next_node
    
    # Function to check if stack is empty
    def isEmpty(self):
        return (self.top_node == None)

    # Function to Push new key onto stack and update top
    def push(self, new_key):
        new_node = Node(new_key)
        new_node.next_node = self.top_node
        self.top_node = new_node
            
    # Function to Pop top node from stack
    def pop(self):
        # Returns None if stack is empty
        if(self.isEmpty()):
            raise Exception("Stack is empty")
        # Pop top node and update next node to be top node
        popped_node = self.top_node
        self.top_node = self.top_node.next_node
        
        return popped_node.key
    
# Input controller
def read_inst(stack, inst):
    inst = [i for i in inst.split()]
    if inst[0] == 'PU':
        stack.push(inst[1])
    if inst[0] == 'PO':
        print(stack.pop())

# Read input for test
N = int(input())
stack = Stack()
inst = []
for i in range(0, N):
    inst.append(str(input()))

for i in range(0, N):
    read_inst(stack, inst[i])

