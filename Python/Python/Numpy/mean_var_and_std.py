import numpy as np

n, m = map(int, input().split())
matrix = np.array([input().strip().split() for _ in range(n)], int)

np.set_printoptions(legacy='1.13')  # the numpy print formatter use the default settings from numpy version 1.13 instead of current numpy version
print(np.mean(matrix, axis=1))
print(np.var(matrix, axis=0))
print(np.std(matrix, axis=None))
