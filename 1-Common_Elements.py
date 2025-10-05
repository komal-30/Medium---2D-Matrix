#Brute Force
def common_elements_bruteforce(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    for num in matrix[0]:
        flag = True
        for i in range(1, rows):
            if num not in matrix[i]:
                flag = False
                break
        if flag:
            result.append(num)
    return result

#Ideal
def common_elements_ideal(matrix):
    freq = {}
    rows = len(matrix)
    
    for i in range(rows):
        for num in set(matrix[i]):  
            freq[num] = freq.get(num, 0) + 1

    result = [num for num, count in freq.items() if count == rows]
    return sorted(result)
        
#Optimal
def common_elements_optimal(matrix):
    common = set(matrix[0])         
    for row in matrix[1:]:          
        common = common.intersection(set(row))
    return sorted(common)

matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
]
print(common_elements_ideal(matrix))