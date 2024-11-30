#concept of matrix in numpy
import numpy as np

matrix = np.matrix([[1,2],[3,4]])
print(matrix)
print()
print()
arr = np.array([[1,2],[3,4]])
print(arr)
print()

matrix_add = matrix + matrix
print(matrix_add)

print()
array_add = arr + arr
print(array_add)

#matrix multiplication
print()
matrix_mul = matrix * matrix
print(matrix_mul)

#array multiplication
print()
arr_mul = arr * arr
print(arr_mul)

#array multiplication is different than matrix multiplication