import numpy as np

first_matrix = np.array([input().strip().split()], int)
second_matrix = np.array([input().strip().split()], int)

print(*np.inner(first_matrix, second_matrix)[0])
print(np.outer(first_matrix, second_matrix))
