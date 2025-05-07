# bfs and dfs
graph = {}  #Initializes an empty dictionary to represent the graph using an adjacency list.

def add_edge(u,v):        #Defines a function to add an edge between nodes u and v.
    if u not in graph:
        graph[u] = []    #If node u is not already in the graph, add it with an empty adjacency list.
    if v not in graph:
        graph[v] = []    #Similarly, ensure node v is also in the graph
    graph[u].append(v)
    graph[v].append(u)   #Since this is an undirected graph, add v to u’s list and u to v’s list.

def dfs(node,visited):
    visited.append(node)
    print(node,end=' ')   # Marks the current node as visited and prints it.
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour,visited)   #For each adjacent node, if it hasn't been visited, call DFS recursively.

def bfs(start):
    visited = [start]
    queue = [start]   #Initializes visited and queue lists with the starting node.
    while queue:
        node = queue.pop(0)
        print(node,end=' ')   #Dequeues the front node and prints it.
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)   #Visits and queues all unvisited adjacent nodes of the current node.

edges = int(input("Enter the no of edges: "))
print("Enter the edges like a b : ")
for _ in range(edges):
    u,v = input().split()
    add_edge(u,v)   #Takes number of edges and builds the graph by taking edge inputs.

start = input("\nEnter starting node")
print("\ndfs")
dfs(start,[])
print("\nbfs")
bfs(start)   #Takes starting node input and calls DFS and BFS.

# INPUT :

# Enter the no of edges: 5
# Enter the edges like a b : 
# 1 2
# 1 3
# 2 4
# 3 5
# 4 5
# Enter starting node 1

# OUTPUT

# dfs
# 1 2 4 5 3
# bfs
# 1 2 3 4 5