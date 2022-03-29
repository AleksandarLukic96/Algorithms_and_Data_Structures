# Aleksandar Lukic

# This is an implementation of a dynamic queue data structure using arrays

# A queue is a dynamic sequence, which supports the operations enqueue(x) and dequeue()
# Think of a line in the super market. In order for you to buy your grocceries, every customer 
# in front of you have to buy their grocceries first.  
# This applies for every one in the queue and thus, you all wait for the people in front.
# This is the idea of the queue data structure.

# In this example, we have implemented a queue that fills the array in a cycle,
# meaning that if the last element is at the last index in the array, then we will
# enqueue the new element into the 0 index in the array, given that this index is not
# the head, in which case the array would be full. 

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1
    
    # Function to print queue
    def print(self):
        print(self.queue)
    
    # Function to increment the pointers
    def increment(self, pointer):
        if pointer == self.size - 1:
            return 0
        return pointer + 1
    
    # Function to check if queue is empty
    def isEmpty(self):
        return (self.queue[self.head] == None and self.queue[self.head] == None)

    # Function to check if queue is full
    def isFull(self):
        return (self.queue[self.head] != None and self.head == self.increment(self.tail))
    
    # Function to Enqueue new key onto queue and update head
    def enqueue(self, new_key):
        # Raises exception if queue is full
        if(self.isFull()):
            raise Exception("Queue is full")
        
        
        if(self.head == -1 and self.tail == -1):
            # Incerement both pointers and insert new value
            self.tail = self.increment(self.tail) 
            self.head = self.increment(self.head)           
            self.queue[self.tail] = new_key
            return

        # Incerement tail-pointer and insert new value
        self.tail = self.increment(self.tail)
        self.queue[self.tail] = new_key
                             
    # Function to Dequeue head node from queue
    def dequeue(self):
        # Raises exception if queue is empty
        if(self.isEmpty()):
            raise Exception("Queue is empty")
        
        # Dequeue head and update next node to be head node
        dequeued_value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = self.increment(self.head) 
        
        return dequeued_value

if __name__ == "__main__": 
    # Input controller
    def read_inst(queue, inst):
        inst = [i for i in inst.split()]
        if inst[0] == 'E':
            queue.enqueue(inst[1])
        if inst[0] == 'D':
            print(queue.dequeue())
        #queue.print()

    # Read input for test
    N = int(input())
    queue = Queue(N)
    inst = [] * N
    for i in range(0, N):
        inst.append(str(input()))

    print("\nDequeued elements:")

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