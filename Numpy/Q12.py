#slicing
#array[starting index of array : ending index of array+1 : steps (mean how many jumps)]
import numpy as np
arr = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8])

#need elements from index 1 to index 5(2 to 6)
print(arr[1 : 5 + 1 : 1])

#from start to value 6
print(arr[ : 5+1 : 1])

#starting from value 5 to end value
print(arr[4 : ])

#print the value for jump of 2
print(arr[ : : 2])

#2D array slicing
arr2 = np.array([[9,8,7,6],[11,12,13,14]])
print(arr2[0 : 2 : ])

arrs2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arrs2[1 : 1 : ])