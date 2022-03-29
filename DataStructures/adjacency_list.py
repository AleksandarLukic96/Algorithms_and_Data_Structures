# Aleksandar Lukic

# This is an implementation of an dynamic adjancency list data structure using Singly-linked lists.

from linked_list_singly import Node as Node
from linked_list_singly import LinkedList as l_list
""" 
class AdjacencyList:
    def __init__(self, size):
        self.size = size
        self.list = [l_list(None)] * size
    
    
    def adjacents():
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node 
 """

class AdjacencyList:
    def __init__(self, size):
        self.size = size
        self.adj_list = [None] * size
        for i in range(0, size):
            self.adj_list[i] = l_list()

    # Add edges
    def add_edge(self, v1, v2):
        self.adj_list[v1].insertAtEnd(v2)
        #self.adj_list[v2].insertAtEnd(v1)
    
    # Function to print out adjacency list
    def print(self):
        for i in range(0, self.size-1):
            arr = []
            self.adj_list[i].toArray(arr, self.adj_list[i].head_node)
            print(str(arr))

if __name__ == "__main__":
    size = 5

    # Create vertecies and edges
    adj_list = AdjacencyList(size)    
    adj_list.add_edge(0, 1)
    adj_list.add_edge(0, 2)
    adj_list.add_edge(0, 3)
    adj_list.add_edge(1, 2)
    adj_list.print()    
    
    
""" 
# Adjacency List representation in Python
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

#        node = AdjNode(s)
#        node.next = self.graph[d]
#        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end = "")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end = "")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
 """    