# Given a nested list representing a 3x3 matrix, write a function
# transpose_matrix that returns a new matrix that is the transpose of the
# original (rows become columns and columns become rows).

def transpose_matrix(matrix):
    zipped = zip(matrix[0], matrix[1], matrix[2])

    new_tuple_matrix = list(zipped)

    result = [list(element) for element in new_tuple_matrix]

    return result

# If we wanted to take an unknown size of matrix?
# get the row
# append the first element of each row to a new list
# nest that list in another list.
# loop again, this time take the 2nd elements of each row to a new list
# nest that new list in the same larger list
# loop again, doing the same thing again till all rows are exhausted.

def transpose_matrix(matrix):
    idx = 0
    outer = []

    while idx < len(matrix):
        inner = [row[idx] for row in matrix]
        
        outer.append(inner)
        idx += 1
    
    return outer

def transpose_matrix(matrix):
    outer = []

    for idx in range(len(matrix)):
        inner = [row[idx] for row in matrix]
        
        outer.append(inner)
    
    return outer

# Expected behavior:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(matrix))
# Should output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]