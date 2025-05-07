# dijkstra algorithm

import heapq  # Imports the heapq module to use a priority queue (min-heap), which helps retrieve the node with the smallest distance efficiently.

def dijkstra(graph,start):
    distances = {node : float('inf') for node in graph}    #Initializes all distances to infinity.
    distances[start] = 0   #Sets the starting node's distance to 0.
    queue = [(0,start)]    # Adds the starting node to the priority queue with cost 0.

    while(queue):
        cost,node = heapq.heappop(queue)    # Pops the node with the smallest distance (greedy choice).
        for neighbour , weight in graph[node]:
            distance = cost + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(queue,(distance,neighbour))
                #  Checks each neighboring node.
# If a shorter path is found, updates the distance and adds to the queue. 
    return distances

#Returns the dictionary of minimum distances from the start node to all others.

graph = {}

def add_edge(u,v,w):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v,w))
    graph[v].append((u,w))

# Initializes an empty graph.
# add_edge() ensures the graph is bidirectional by storing each connection both ways.

edges = int(input("Enter the no of edges : "))
print("Enter Edges like a b 2")
for _ in range(edges):
    u,v,w = input().split()
    add_edge(u,v,int(w))

# Reads number of edges.
# Accepts edge input in the form (node1, node2, weight).

start = input("Enter the starting node : ")
print(dijkstra(graph,start))

#Takes starting node input and runs the algorithm.

#INPUT : 

# Enter the no of edges : 5
# Enter Edges like a b 2
# A B 4
# A C 2
# B C 5
# B D 10
# C D 3
# Enter the starting node : A

#OUTPUT :

#{'A': 0, 'B': 4, 'C': 2, 'D': 5}
