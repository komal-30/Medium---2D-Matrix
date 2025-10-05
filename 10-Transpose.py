#Brute Force
def transpose_bruteforce(matrix):
    m, n = len(matrix), len(matrix[0])
    transposed = [[0]*m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    
    return transposed


#Ideal
def transpose_ideal(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

#Optimal
def transpose_optimal(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
