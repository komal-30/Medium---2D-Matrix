#Brute Force
def row_with_max_ones_bruteforce(matrix):
    max_count = -1
    row_index = -1
    for i, row in enumerate(matrix):
        count = sum(row)
        if count > max_count:
            max_count = count
            row_index = i
    return row_index


#Ideal
def row_with_max_ones_binary(matrix):
    def first_one_index(row):
        low, high = 0, len(row)-1
        index = len(row)
        while low <= high:
            mid = (low + high)//2
            if row[mid] == 1:
                index = mid
                high = mid - 1
            else:
                low = mid + 1
        return index
    
    max_count = -1
    row_index = -1
    for i, row in enumerate(matrix):
        idx = first_one_index(row)
        count = len(row) - idx
        if count > max_count:
            max_count = count
            row_index = i
    return row_index


#Optimal
def row_with_max_ones_optimal(matrix):
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n-1
    max_row = -1

    while row < m and col >= 0:
        if matrix[row][col] == 1:
            max_row = row
            col -= 1
        else:
            row += 1
    return max_row