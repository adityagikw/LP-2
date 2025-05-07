# a star algorithm
import heapq  #Imports the heap queue module to use a priority queue (min-heap), essential for A*.

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  #This is the Manhattan distance heuristic. It estimates the cost from node a to node b

def astar(grid,start,goal):  #The main function implementing the A* algorithm. Takes a 2D grid, start, and goal positions.
    rows,cols = len(grid) , len(grid[0])  #Determines the size of the grid.
    visited = set()  #Keeps track of visited nodes to prevent revisiting.
    open_list = [(0+heuristic(start,goal),0,start,[])]   #Priority queue (min-heap) with tuples (f, g, current_node, path_so_far). f = g + h.

    while(open_list):   #Continues while there are nodes to explore.
        f,g,current,path = heapq.heappop(open_list)   #Pops the node with the lowest f-score.

        if current in visited:
            continue    #Skip if the node has already been processed.
        visited.add(current)
        path = path+[current]  #Mark the node as visited and update the path.

        if current == goal:
            return path    #Goal check: if reached, return the path.
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:    #Explore all 4 directions: up, down, left, right.
            nx,ny = current[0]+dx , current[1]+dy    #Compute the neighbor’s coordinates.
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:    #Check if the neighbor is within bounds and is not a wall (0 = walkable).
                neighbour = (nx,ny)
                if neighbour not in visited:
                    heapq.heappush(open_list,(g+1+heuristic(current,goal),g+1,neighbour,path))  #Push the neighbor into the open list with its updated f-score.
    return None  #If goal is not found, return None

grid = eval(input("Enter the grid like [[1,2,3,4],[5,6,7,8]].. : "))
print("grid entered : ")
for row in grid:
    print(row)

start = eval(input("Enter the start state like (0,0) : "))
goal = eval(input("Enter the Goal state like (1,5) : "))

path = astar(grid,start,goal)
if path:
    for p in path:
        print(p)
else:
    print("No path found")

#INPUT :

# Enter the grid like [[1,0,0],[1,0,1],[1,0,0]].. : [[0,0,0],[1,1,0],[0,0,0]]
# Enter the start state like (0,0) : (0,0)
# Enter the Goal state like (1,5) : (2,2)

#OUTPUT :

# (0, 0)
# (0, 1)
# (0, 2)
# (1, 2)
# (2, 2)