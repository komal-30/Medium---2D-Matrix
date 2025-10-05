#Brute Force
def rotate_matrix_bruteforce(matrix):
    n = len(matrix)
    rotated = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    
    return rotated

#Ideal
def rotate_matrix_ideal(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

#Optimal
def rotate_matrix_optimal(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save top
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
    return matrix