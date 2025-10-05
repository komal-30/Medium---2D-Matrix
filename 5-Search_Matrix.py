#Brute Force
def search_matrix_bruteforce(matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False

#Ideal / Optimal
def search_matrix_stepwise(matrix, target):
    if not matrix: 
        return False
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1
    
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False


