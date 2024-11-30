import numpy as np

#shape
#shape is used to identify the number of column and rows in a matrix
arr = np.array([1,2,3,4,5])
print(arr.shape)

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.shape)

#reshape
#reshape is used to convert the dimension into another dimension
print(np.reshape(arr1,(1,6)))
print(np.reshape(arr1,(3,2)))

#reshape a normal array into 3d array
arr2 =  np.array([1,2,3,4,5,6,7,8,9])
arr3 = np.reshape(arr2,(3,3))
#to convert multiple dimension into 1D
arr4 = np.reshape(arr3,(-1))
arr5 = np.ravel(arr3)
print(arr2)
print(arr3)
print(arr4)
print(arr5)