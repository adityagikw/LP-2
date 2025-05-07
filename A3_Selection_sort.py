
# selection sort

def selection_sort():   #Defines a function named selection_sort. The code inside this function will only execute when the function is called.
    n = int(input("Enter the total no in an array : "))  #Takes user input for the number of elements in the array and converts it to an integer.
    arr = []    #Initializes an empty list to store array elements.
    for i in range(n):
        val = int(input(f"Enter val {i} : "))
        arr.append(val)   #A loop runs n times to take n values from the user and appends them to the array.
    
    for i in range(n):
        mini = i   #Outer loop starts from 0 to n-1. mini is the index of the smallest element found.
        for j in range(i+1,n):
            if(arr[mini]>arr[j]):
                mini = j   #Inner loop finds the index of the smallest element from i+1 to n-1 and stores it in mini.
        arr[i],arr[mini] = arr[mini],arr[i]  #Swaps the current element with the smallest found in the unsorted part of the array.
    print("selection sort",arr)

selection_sort()  #Calls the function to execute the selection sort process.

#INPUT : 

# n = 5

# values: 29, 10, 14, 37, 13

#OUTPUT :

# Initial: [29, 10, 14, 37, 13]

# Pass 1: [10, 29, 14, 37, 13]

# Pass 2: [10, 13, 14, 37, 29]

# Pass 3: [10, 13, 14, 29, 37]

# Pass 4: [10, 13, 14, 29, 37] (already sorted)

# Final Output : selection sort [10, 13, 14, 29, 37]
