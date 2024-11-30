#indexing 
import numpy as np
arr = np.array([1 , 2 , 3 , 4])

#if i access the last element of the array without using loop
last_element = arr[-1]
print(last_element)

arr1 = np.array([[9 , 8 , 7],[4 , 5 , 6]])
print(arr1)
print(arr1[1][1])   #it will print 5 the first index show the block and the second index show the element of second block
print(arr1[1 , 1]) #second metheod the first element show row address and the second element show element address

#to get 8
print(arr1[0 , 1])

#3D array 
arr3 = np.array([[[1 , 2],[3 , 4]]])
print(arr3[0 , 0 , 1]) #first show block address second show row address third show element address

#4D array

arr4 = np.array([[[[1 , 2],[3 , 4]]]])
print(arr4[0 , 0 , 1 , 1 ])