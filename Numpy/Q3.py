import numpy as np

#creating array whose all elements are zero
arr0 = np.zeros(4)
print(arr0)

#creating matrix whose all elements are zero
matrix_zero = np.zeros((5,10))
print("matrix : ",matrix_zero)


#creating array whose all elments are one
arr1 = np.ones(5)
print(arr1)
list = arr1.tolist()
print(list)

#creating a matrix whose all elements are 1
matrix_one = np.ones((5,3))
print("matrix : ",matrix_one)

#creating an empty array
arrnull = np.empty(4)
print(arrnull)

#range array will create array from zerro to 9 elements
arr_range = np.arange(10)
print(arr_range)

#diagonal element of 3x3 matrix
diagonal = np.eye(3)
print(diagonal)
print(diagonal.ndim)

#linespace element 
line_arr = np.linspace(0,20,num=5)
print(line_arr)