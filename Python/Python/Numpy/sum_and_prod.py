import numpy as np

'''
my_array = numpy.array([ [1, 2], [3, 4] ])
print(my_array)
print(numpy.sum(my_array, axis = 0))
print(numpy.sum(my_array, axis = 1))
print(numpy.sum(my_array, axis = None))
print(numpy.sum(my_array))

print(numpy.prod(my_array, axis = 0))
print(numpy.prod(my_array, axis = 1))
print(numpy.prod(my_array, axis = None))
print(numpy.prod(my_array))
'''

n, m = map(int, input().strip().split())
matrix = np.array([input().strip().split() for _ in range(n)], int)
sum_list = np.sum(matrix, axis=0)
print(np.product(sum_list))
