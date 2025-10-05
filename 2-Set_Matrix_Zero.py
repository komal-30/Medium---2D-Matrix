#Brute Force
def set_matrix_zero_bruteforce(matrix):
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                for x in range(m):
                    if matrix[x][j] != 0:
                        matrix[x][j] = None
                for y in range(n):
                    if matrix[i][y] != 0:
                        matrix[i][y] = None
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] is None:
                matrix[i][j] = 0
    return matrix

#Ideal
def set_matrix_zero_ideal(matrix):
    m, n = len(matrix), len(matrix[0])
    rows = [False]*m
    cols = [False]*n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0

    return matrix

#Optimal
def set_matrix_zero_optimal(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

print(set_matrix_zero_bruteforce([row[:] for row in matrix]))
print(set_matrix_zero_ideal([row[:] for row in matrix]))
print(set_matrix_zero_optimal([row[:] for row in matrix]))