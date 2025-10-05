#Brute Force
def max_sum_rectangle_bruteforce(matrix):
    m, n = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    
    for row1 in range(m):
        for col1 in range(n):
            for row2 in range(row1, m):
                for col2 in range(col1, n):
                    curr_sum = sum(matrix[i][j] for i in range(row1, row2+1) for j in range(col1, col2+1))
                    max_sum = max(max_sum, curr_sum)
                    
    return max_sum

#Ideal
def max_sum_rectangle_kadane(matrix):
    m, n = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    
    for top in range(m):
        temp = [0]*n
        for bottom in range(top, m):
            for col in range(n):
                temp[col] += matrix[bottom][col]
            
            curr_sum = temp[0]
            max_curr = temp[0]
            for val in temp[1:]:
                curr_sum = max(val, curr_sum + val)
                max_curr = max(max_curr, curr_sum)
            max_sum = max(max_sum, max_curr)
            
    return max_sum

#Optimal
def max_sum_rectangle_easy(matrix):
    m, n = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    
    for top in range(m):
        temp = [0] * n  
        for bottom in range(top, m):
            for col in range(n):
                temp[col] += matrix[bottom][col]
            curr = 0
            for val in temp:
                curr = max(val, curr + val)
                max_sum = max(max_sum, curr)
    
    return max_sum