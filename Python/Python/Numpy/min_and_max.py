import numpy as np

n, m = map(int, input().strip().split())
matrix = np.array([input().strip().split() for _ in range(n)], int)
min_in_row = np.min(matrix, axis=1)
print(np.max(min_in_row))
