# Aleksandar Lukic

# This is an implementation of a dynamic queue data structure using Singly-linked lists

# A queue is a dynamic sequence, which supports the operations enqueue(x) and dequeue()
# Think of a line in the super market. In order for you to buy your grocceries, every customer 
# in front of you have to buy their grocceries first.  
# This applies for every one in the queue and thus, you all wait for the people in front.
# This is the idea of the queue data structure.

class Node:
   def __init__(self, key = None):
      self.key = key
      self.next_node = None

class Queue:
    def __init__(self):
      self.head_node = None
      self.tail_node = None
    
    # Function to print queue
    def print(self):
        current_node = self.head_node
        while (current_node != None):
            print(current_node.key)
            current_node = current_node.next_node
    
    # Function to check if queue is empty
    def isEmpty(self):
        return (self.head_node == None)

    # Function to Enqueue new key onto queue and update head
    def enqueue(self, new_key):
        new_node = Node(new_key)
        if (self.head_node == None):
            self.head_node = new_node
            self.tail_node = new_node
            return
        self.tail_node.next_node = new_node 
        self.tail_node = new_node 
          
    # Function to Pop head node from queue
    def dequeue(self):
        # Returns None if queue is empty
        if(self.isEmpty()):
            raise Exception("Queue is empty")
        # Pop head node and update next node to be head node
        dequeued_node = self.head_node
        self.head_node = self.head_node.next_node
        
        return dequeued_node.key
    
# Input controller
def read_inst(queue, inst):
    inst = [i for i in inst.split()]
    if inst[0] == 'E':
        queue.enqueue(inst[1])
    if inst[0] == 'D':
        print(queue.dequeue())

# Read input for test
N = int(input())
queue = Queue()
inst = []
for i in range(0, N):
    inst.append(str(input()))

for i in range(0, N):
    read_inst(queue, inst[i])
    
# Copy and paste test input for terminal:
""" 
10
E 1
E 2
D
E 3
D
D
E 4
D
E 5
E 6
"""
# Expected output in terminal:
# 1
# 2
# 3
# 4