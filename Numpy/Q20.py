#matrix function in numpy array (transpose , swapaxes , inverse , power , determinate , dot product , cross product)
import numpy as np

matrix = np.matrix([[1,2],[3,4],[5,6]])
print(matrix)

#transpose of matrix
transpose = np.transpose(matrix)
print(transpose)

#inverse of a matrix 
mat = np.matrix([[1,2],[3,4]])
inverse = np.linalg.inv(mat)
print(mat)
print(inverse)

#power of a matrix
print(np.linalg.matrix_power(mat,2))

#determinate of matrix
matr = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
det_matrix = np.linalg.det(matr)
print()
print(matr)
print()
print(det_matrix)

#dot product
matri = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
dot = np.dot(matri , matri) #dot product is same as matrix multiplication
print(matri)
print(dot)

#cross prduct b x c
b = np.matrix([1,1,2])
c = np.matrix([-2,1,-3])
A = np.linalg.cross(b,c)
print(A)