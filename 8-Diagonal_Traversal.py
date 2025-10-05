#Brute Force
from collections import defaultdict
def diagonal_traversal_bruteforce(matrix):
    if not matrix:
        return []
    
    diagonals = defaultdict(list)
    m, n = len(matrix), len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            diagonals[i+j].append(matrix[i][j])
    
    result = []
    for d in range(m + n - 1):
        if d % 2 == 0:
            result.extend(reversed(diagonals[d]))
        else:
            result.extend(diagonals[d])
    
    return result


#Ideal
def diagonal_traversal_ideal(matrix):
    if not matrix:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    
    for d in range(m + n - 1):
        temp = []
        for i in range(m):
            for j in range(n):
                if i + j == d:
                    temp.append(matrix[i][j])
        if d % 2 == 0:
            temp.reverse()
        result.extend(temp)
    
    return result


#Optimal
def diagonal_traversal_optimal(matrix):
    if not matrix:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    row = col = 0
    up = True  
    
    while len(result) < m * n:
        result.append(matrix[row][col])
        
        if up:
            if col == n - 1:
                row += 1
                up = False
            elif row == 0:
                col += 1
                up = False
            else:
                row -= 1
                col += 1
        else:
            if row == m - 1:
                col += 1
                up = True
            elif col == 0:
                row += 1
                up = True
            else:
                row += 1
                col -= 1
    
    return result