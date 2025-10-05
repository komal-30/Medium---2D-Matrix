#Brute Force
def kth_smallest_bruteforce(matrix, k):
    flat = [num for row in matrix for num in row]
    flat.sort()
    return flat[k-1]

#Ideal 
import heapq

def kth_smallest_ideal(matrix, k):
    m, n = len(matrix), len(matrix[0])
    heap = []

    for i in range(min(k, m)):
        heapq.heappush(heap, (matrix[i][0], i, 0))  

    for _ in range(k-1):
        val, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c+1], r, c+1))

    return heapq.heappop(heap)[0]

#Optimal
def kth_smallest_optimal(matrix, k):
    n = len(matrix)

    def count_less_equal(mid):
        count, row, col = 0, n-1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    low, high = matrix[0][0], matrix[-1][-1]
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

matrix = [[1,5,9], [10,11,13], [12,13,15]]
k = 8

print(kth_smallest_bruteforce(matrix, k))      
print(kth_smallest_ideal(matrix, k))            
print(kth_smallest_optimal(matrix, k))