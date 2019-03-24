import numpy as np

n = int(input())

first_matrix = np.array([input().strip().split() for _ in range(n)], int)
second_matrix = np.array([input().strip().split() for _ in range(n)], int)
# print(np.matmul(first_matrix, second_matrix))
print(np.dot(first_matrix, second_matrix))
