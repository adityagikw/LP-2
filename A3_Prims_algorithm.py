# prims algorithm

import heapq  #Imports the heapq module for priority queue implementation (min-heap).

def primsalgo(graph,start):  #Defines the Prim’s algorithm function.
    visited = set()   #Set to keep track of visited nodes
    min_heap = [(0,start)]   #Priority queue with (weight, node) format. Initialized with (0, start)
    mst_count = 0   #Stores total weight of the Minimum Spanning Tree (MST).

    while(min_heap):  #While heap is not empty:
        cost,node = heapq.heappop(min_heap)  #Pops the edge with the minimum weight.
        if node not in visited:
            visited.add(node)
            mst_count += cost   #If the node is unvisited, mark as visited and add its cost to MST.
        for neighbour,weight in graph[node]:  #For each neighbor of the current node:
            if neighbour not in visited:
                heapq.heappush(min_heap,(weight,neighbour))  #If not visited, push the edge to the heap.
    return mst_count   #Returns total cost of the MST.

graph = {}    #Initializes the graph as an adjacency list (dictionary).
def add_edge(u,v,w):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v,w))
    graph[v].append((u,w))  #Adds an undirected edge between node u and v with weight w.

edge = int(input("Enter the number of edges : "))
print("Enter the edge like A B 4")
for _ in range(edge):
    u,v,w = input().split()
    add_edge(u,v,int(w))

# Takes user input for number of edges.

# Each edge is input as: Node1 Node2 Weight (e.g., A B 4).

start = input("Enter the start node : ")

print(primsalgo(graph,start))

# Asks for the starting node.

# Calls Prim’s algorithm and prints the MST weight.

#INPUT : 

# Enter the number of edges : 5
# Enter the edge like A B 1
# A B 1
# B C 3
# A C 2
# C D 4
# B D 5
# Enter the start node : A

# GRAPH : 

#      1        3
# A ------ B ------- C
#  \      |         /
#   \     |        /
#    \    |5      /4
#     \   |     /
#      \  |   /
#        D
# Prim’s MST edges: A–B(1), A–C(2), C–D(4)
# Total weight = 1 + 2 + 4 = 7


#OUTPUT : 

# 7