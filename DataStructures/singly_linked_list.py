# Aleksandar Lukic 

# Singly-Linked Lists
# A linked list is a data structure which maintains a dynamic sequence of elements.
# The sequence order is determined by pointers/references in memory, called "links".
# The nodes in a Singly-linked list only have a single reference, 
# to the following node.
# Thus, it is not possible to search backwards in these lists.
 

class Node:
   def __init__(self, key = None):
      self.key = key
      self.next_node = None

class SinglyLinkedList:
    def __init__(self):
      self.head_node = None

    # Function to lookup given key
    def search(self, key):
        current_node = self.head_node
        while(current_node != None):
            if(current_node.key == key):
                return current_node
            current_node = current_node.next_node
        return None
    
    # Function to print linked list
    def print(self):
        current_node = self.head_node
        while (current_node.next_node != None):
            print(current_node.key)
            current_node = current_node.next_node
    
    # Function to insert key in front of head
    def insertAtBegining(self, new_key):
        # Create new node with given key
        new_node = Node(new_key)

        # Update new_node with head_node as next_node
        new_node.next_node = self.head_node
        self.head_node = new_node
    
    # Function to insert key in front of head
    def insertAtEnd(self, new_key):
        # Create new node with given key
        new_node = Node(new_key)

        current_node = self.head_node
        
        # Find end of singly-linked list
        while (current_node.next_node != None):
            current_node = current_node.next_node
        
        # Insert new node after the last node in the singly-linked list
        current_node.next_node = new_node
    
    # Function to insert key in between nodes in list
    def insertInbetween(self, lookup_node, new_key):
        if(self.search(lookup_node.key) == None):
            return None
    
        new_node = Node(new_key)
        new_node.next_node = lookup_node.next_node
        lookup_node.next_node = new_node
    
    def deleteNode(self, key):
        current_node = self.head_node
        while(current_node != None):
            if(current_node.next_node.key == key):
                current_node.next_node = current_node.next_node.next_node
                break    
            current_node = current_node.next_node
        return
            
# Test nodes
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
node4 = Node("Thursday")
node5 = Node("Friday")
node6 = Node("Saturday")
node7 = Node("Sunday")

# Create Singly-linked list object and initialize head node
singly_linked_list = SinglyLinkedList()
singly_linked_list.head_node = node2

# Link node to head node
singly_linked_list.head_node.next_node = node3

# Link Nodes together
node3.next_node = node4
node4.next_node = node5
node5.next_node = node6

# Insert keys to begining and end of linked list
singly_linked_list.insertAtBegining(node1.key)
singly_linked_list.insertAtEnd(node7.key)
singly_linked_list.insertInbetween(node3, node3.key)
singly_linked_list.deleteNode(node3.key)
singly_linked_list.print()
