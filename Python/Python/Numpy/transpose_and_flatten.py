import numpy as np

n, m = map(int, input().strip().split())
arr = np.array([input().strip().split() for _ in range(n)], int)

print(arr.transpose())
print(arr.flatten())
