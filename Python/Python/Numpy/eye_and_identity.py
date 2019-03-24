import numpy as np

'''
print(np.identity(3))
print(np.eye(8, 7, k = 1))
'''
n, m = np.array(input().split(), int)
np.set_printoptions(legacy='1.13')  # the numpy print formatter use the default settings from numpy version 1.13 instead of current numpy version
print(np.eye(n, m, k=0))
