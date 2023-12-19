def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal_sum = sum(arr[i][i] for i in range(n))
    secondary_diagonal_sum = sum(arr[i][n-i-1] for i in range(n))
    return abs(primary_diagonal_sum - secondary_diagonal_sum)
matrix_size = int(input().strip())
matrix = []
for _ in range(matrix_size):
    row = list(map(int, input().split()))
    matrix.append(row)
result = diagonalDifference(matrix)
print(result);