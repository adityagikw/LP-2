def issafe(arr,x,y,n):   #Checks whether placing a queen at position (x, y) is safe.
    for row in range(x):
        if arr[row][y] ==1:
            return False
        
        #Checks if any queen exists in the same column above the current row.

    row = x
    col = y
    #Checking Diagonal Attack
    while row>=0 and col>=0:
        if arr[row][col]==1:
            return False
        row-=1
        col-=1

        #Checks upper-left diagonal for any attacking queen.

    row = x
    col = y
    #Checking Anti Diagonal Attack
    while row>=0 and col<n:
        if arr[row][col]==1:
            return False
        row-=1
        col+=1

        #Checks upper-right (anti-diagonal) direction.

    return True  #Returns True if all checks pass.

def nQueen(arr,x,n):  #Main recursive function to place queens from row x to row n-1.
    if x>=n:
        return True   #If all queens are placed, return True.

    for col in range(n):   #Try placing queen in each column of row x.
        if issafe(arr,x,col,n):
            arr[x][col]=1    #If safe, place queen.
            if nQueen(arr,x+1,n):
                return True  #Make recursive call to place queen in next row.
            arr[x][col] = 0  #Backtrack (remove queen) if it leads to failure.

    return False   #If no column is safe in this row, return False.

def main():
    n = int(input("Enter number of Queens : "))  #Takes input from user for N.
    arr = [[0]*n for i in range(n)]   #Initializes an empty N×N board with 0s.

    if nQueen(arr,0,n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j],end=" ")
            print()

#If a valid solution is found, print the board.


if __name__ == '__main__':
    main()

#INPUT : 

#Enter number of Queens : 4

#OUTPUT : 

# 0 1 0 0 
# 0 0 0 1 
# 1 0 0 0 
# 0 0 1 0 
