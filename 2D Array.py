# Declaration of a Matrix or two-dimensional array is very much similar to that of a one-dimensional array

# Defining number of rows and columns of a matrix
rows = 3
cols = 3

# Declaring a matrix of size 3x3, and
# Initializing it with value zero
rows, cols = (3,3)
arr = [[0]*cols]*rows
print(arr)


# In Initialization, we assign some initial value to all the cells of the matrix

# Initializing a 2D array
arr = [[1,2,3],[4,5,6],[7,8,9]]


# Like one-dimensional arrays, matrices can be accessed randomly by using their indices to access the individual elements
# A cell has two indices, one for its row number, and the other for its column number
# We can use arr[i][j] to access the element which is at the ith row and jth column of the matrix

# Initializing array with values
arr = [[1,2,3],[4,5,6],[7,8,9]]

#Accessing elements of 2-D array

print("First element of first row: ", arr[0][0])
print("Second element of third row: ",arr[2][1])
print("Third Element of second row: ",arr[1][2])


# We can traverse all the elements of a matrix or two-dimensional array by using two for-loops

# Initializing a 2D array list with values
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# Traversing each row
for row in arr:

    # Traversing each element
    # in the current row
    for x in row:
        print(x, end = " ")
    print()


# We can search an element in a matrix by traversing all the elements of the matrix

# Function to search an element in a 2D List
def search_in_matrix(arr, x):
    rows, cols = len(arr), len(arr[0])

    # Traverse each row and column
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == x:
                return True
    return False

# Driver code to test the function
x = 8
arr = [[0,6,8,9,11],[20,22,28,29,31],[36,38,50,61,63],[64,66,100,122,128]]

if(search_in_matrix(arr,x)):
    print("YES")
else:
    print("NO")