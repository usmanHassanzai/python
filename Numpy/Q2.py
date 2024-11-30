import numpy as np

#1D array
arr1 = np.array([1,2,3,4,5])
print(arr1)
#checking the dimension of array
print(arr1.ndim)

#2D array
arr2 = np.array([[1,2,3,4,5]])
print(arr2)
print(arr2.ndim)

#10D array
arr10 = np.array([1,2,3,4,5,6] , ndmin = 10)    #ndmin is used for number of dimension
print(arr10)

#2D array of two vectors
arr2v = np.array([[1,2,3,4],[5,6,7,8]],ndmin = 10)
print(arr2v)
print(arr2v.ndim)
#convert 10D into 1D
arr1v = arr2v.ravel()
print(arr1v)
