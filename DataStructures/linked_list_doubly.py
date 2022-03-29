# Aleksandar Lukic 

# Doubly-Linked Lists
# A linked list is a data structure which maintains a dynamic sequence of elements.
# The sequence order is determined by pointers/references in memory, called "links".
# The nodes in a Doubly-linked list have a reference to their prior node 
# and to the following node.
# Thus, it is possible to traverse in both directions, in contrast to sinlgy-linked lists.
 

class Node:
   def __init__(self, key = None):
      self.key = key
      self.prev_node = None
      self.next_node = None

class LinkedList:
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
    
    # Function to print linked list linearly
    def print_linear(self):
        current_node = self.head_node
        while (current_node != None):
            print(current_node.key)
            current_node = current_node.next_node

    # Function to print linked list recursivly
    def print_recursive(self, current_node):
        if current_node == None:
            return
        print(current_node.key)
        self.print_recursive(current_node.next_node)

    
    # Function to insert new node with given key in front of head node
    def insertAtBegining(self, new_node):
        # Link new_node with head_node
        new_node.next_node = self.head_node
        self.head_node.prev_node = new_node
        self.head_node = new_node
    
    # Function to insert new node with given key at the end of the linked list
    def insertAtEnd(self, new_node):
        # Initialize pointer to head node in linked list
        current_node = self.head_node
        
        # Find end of the linked list
        while (current_node.next_node != None):
            current_node = current_node.next_node
        
        # Insert new node after the last node in the linked list
        current_node.next_node = new_node
        new_node.prev_node = current_node 
        
    # Function to insert a new node with given key before a given key in list
    def insertBefore(self, lookup_key, new_node):
        # Lookup the node to place new node before
        lookup_node = self.search(lookup_key)
        if(lookup_node == None):
            return None
        
        # Update new node
        new_node.prev_node = lookup_node.prev_node
        new_node.next_node = lookup_node
        
        # Store node prior to lookup node
        temp_prev_node = lookup_node.prev_node
        
        # Update lookup node
        lookup_node.prev_node = new_node
        
        # In case lookup node is head node, new node becomes head node
        if(lookup_node == self.head_node):
            # Update node prior to lookup node
            self.head_node = new_node
            return
        
        # New node is put after prior node
        temp_prev_node.next_node = new_node

    # Function to insert a new node with given key after a given key in list
    def insertAfter(self, lookup_key, new_node):
        # Lookup the node to place new node after
        lookup_node = self.search(lookup_key)
        if(lookup_node == None):
            return None
        
        # Update new node
        new_node.prev_node = lookup_node
        new_node.next_node = lookup_node.next_node
        
        # If lookup node is not the last node in the list
        if(lookup_node.next_node != None):
            # Update node after the lookup node
            lookup_node.next_node.prev_node = new_node
        
        # Update lookup node
        lookup_node.next_node = new_node

    # Function to delete a node with given key
    def deleteNode(self, lookup_key):
        lookup_node = self.search(lookup_key)
        if lookup_node == None:
            raise Exception("Node not found in linked list!")
        
        # If deleting node is head
        if self.head_node == lookup_node:
            self.head_node = lookup_node.next_node
            lookup_node = None
            return
        
        if lookup_node.next_node == None:
            lookup_node.prev_node.next_node = None
            return
        
        # Get the two neighbour nodes 
        prev_node = lookup_node.prev_node
        next_node = lookup_node.next_node
        
        # Link the two neighbour nodes together
        prev_node.next_node = next_node
        next_node.prev_node = prev_node
            
        # Note that in this example, the deleted node is only detatched from the list,
        # not deleted from memory! This can be done, but for the sake of understanding
        # the concept of linked lists, this step has been left out. 
            
# Test nodes
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
node4 = Node("Thursday")
node5 = Node("Friday")
node6 = Node("Saturday")
node7 = Node("Sunday")
node8 = Node("Happy birthday!")

# Create Doubly-linked list object and initialize head node
linked_list = LinkedList()
linked_list.head_node = node4

# Demo of operations to make linked list
linked_list.insertAtBegining(node2)
linked_list.insertAtEnd(node6)
linked_list.insertBefore(node4.key, node3)
linked_list.insertBefore(node2.key, node1)
linked_list.insertAfter(node4.key, node5)
linked_list.insertAfter(node6.key, node7)

linked_list.insertAtEnd(node8)
linked_list.deleteNode(node8.key)

# In the case where we try to add the head node after any other nodes whithin the list,
# we create a cycle, which means that the head looses its functionality.
# When doing this, the print will continue endlessly, as there will never be a None.
# Try it yourself! To stop the endless printing in the Terminal: CTRL + C 
#
#linked_list.insertAtEnd(node1)

linked_list.print_recursive(linked_list.head_node)
