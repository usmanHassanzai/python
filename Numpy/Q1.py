#creating a numpy array

import numpy as np
from pympler import asizeof
import pympler.asizeof 

#creating array 
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
x=asizeof.asizeof(arr)
print(x)

#creating list
list = [1,2,3,4,5]
print(list)
print(type(list))
print(asizeof.asizeof(list))

#converting array into list
l = arr.tolist()
print(l)

#converting list into array
a = np.array(l)
print(a)