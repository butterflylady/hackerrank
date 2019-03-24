import numpy as np

n, m = map(int, input().strip().split())
first_matrix = np.array([input().strip().split() for _ in range(n)], int)
second_matrix = np.array([input().strip().split() for _ in range(n)], int)
print(np.add(first_matrix, second_matrix))
print(np.subtract(first_matrix, second_matrix))
print(np.multiply(first_matrix, second_matrix))
print(first_matrix // second_matrix)
print(np.mod(first_matrix, second_matrix))
print(np.power(first_matrix, second_matrix))
