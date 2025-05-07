# kruskal algortihm

def find(parent,node):
    if(parent[node]==node):
        return node
    return find(parent,parent[node])

# Purpose: This function performs the Find operation in the Disjoint Set Union (DSU) data structure, which is used to identify the root of a node.

# Explanation: If the parent of a node is the node itself, it's the root of the set, so we return the node. If not, we recursively find the root of the parent node.

def union(parent,u,v):
    root_u = find(parent,u)
    root_v = find(parent,v)

    if(root_u != root_v):
        parent[root_v] = root_u
        return True
    return False

# Purpose: This function performs the Union operation in the Disjoint Set Union (DSU) data structure. It combines two sets if they are not already connected.

# Explanation: We first find the roots of u and v. If the roots are different, we attach one set to the other (we arbitrarily make root_v a child of root_u), and the two sets are merged. If the roots are the same, the nodes are already in the same set, and no action is performed.

def kruskal(vertices,edges):
    edges.sort(key = lambda x:x[2])
    mst = []
    total_cost = 0
    parent = {v : v for v in vertices}

    for u,v,w in edges:
        if(union(parent,u,v)):
            mst.append((u,v,w))
            total_cost += w
    return mst,total_cost

#Purpose: This is the main function that runs Kruskal's algorithm. It returns the Minimum Spanning Tree (MST) and the total cost of the MST.

#Explanation:

# Sort the edges: The edges are sorted by their weight in ascending order to process the minimum weight edge first.

# Initialize the parent dictionary: Each vertex is initially its own parent (disjoint sets).

# Loop through edges: For each edge, the union() function is called. If the edge does not form a cycle (i.e., union() returns True), the edge is added to the MST, and its weight is added to the total cost.

vertices = []
edges = []

# Explanation: Here, two empty lists vertices and edges are initialized.

# vertices: Will store the list of vertices (nodes) in the graph.

# edges: Will store the list of edges, where each edge is represented as a tuple (u, v, w) where u and v are the vertices connected by the edge and w is the weight of the edge.

vcount = int(input("Enter the number of vertices : "))   #The program prompts the user to input the number of vertices (vcount). This value will dictate how many vertices the graph will have.
print("Enter the edge like a b c : ")
for _ in range(vcount):
    vertices.append(input().strip())

#Explanation:

# The program prints a message to the user, indicating that they should enter the vertex names.

# The for _ in range(vcount) loop runs vcount times (based on the number of vertices). During each iteration:

# input() is used to get the name of a vertex from the user.

# strip() removes any leading or trailing whitespace from the input.

# The vertex is then added to the vertices list.

# For example, if you enter 4 vertices, the user might input A, B, C, D (each on a separate line).

ecount = int(input("Enter the number of edges : "))   #The program prompts the user to input the number of edges (ecount). This value will dictate how many edges the graph will have.
print("Enter the edge like a b 2 : ")
for _ in range(ecount):
    u,v,w = input().split()
    edges.append((u,v,int(w)))

# Explanation:

# The program prints a message to the user, instructing them to input the edges in the format u v w where u and v are the vertices connected by the edge, and w is the weight of the edge.

# The for _ in range(ecount) loop runs ecount times (based on the number of edges). During each iteration:

# input() is used to get the edge input from the user.

# split() splits the input string into three parts, u, v, and w. The w is converted into an integer using int().

# A tuple (u, v, w) representing the edge is appended to the edges list.

mst , cost = kruskal(vertices,edges)

# Explanation: The program calls the kruskal() function (which is defined earlier in the code) with vertices and edges as arguments.

# This function will return two values: mst (the Minimum Spanning Tree) and cost (the total cost of the MST).

# mst is a list of edges that form the Minimum Spanning Tree, and cost is the sum of the weights of those edges.

print("cost",cost)
for r in mst:
    print(r)

# This loop iterates through the edges in the Minimum Spanning Tree mst and prints each edge in the format (u, v, w) where u and v are the vertices connected by the edge and w is the weight of the edge.

#INPUT : 

# Enter the number of vertices : 4
# Enter the edge like a b c : 
# A
# B
# C
# D
# Enter the number of edges : 5
# Enter the edge like a b 2 : 
# A B 1
# A C 3
# B C 2
# C D 4
# B D 5


#OUTPUT : 

# cost 7
# ('A', 'B', 1)
# ('B', 'C', 2)
# ('C', 'D', 4)
