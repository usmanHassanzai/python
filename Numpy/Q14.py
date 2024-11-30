#Copy vs View

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print("original array : ",arr)

copy = np.copy(arr)
print("copy of original array : ",copy)

#copy array is a new array when we not affect changin on original array

view = arr.view()
print("view of original array : ",view)
#view array is just view if we change in view it will affect on original array
view[2] = 5
print(view)
print(arr)