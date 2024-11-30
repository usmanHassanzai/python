#Arithmatic function in numpy array (unique , resize , shuffle , flatten , ravel ) not include insert and delete
import numpy as np
arr = np.array([1,2,3,4,10,2,7,4,3,5,6,7])
print(np.unique(arr))
#shuffle
np.random.shuffle(arr)
print(arr)

#resize
print(len(arr))
print(np.resize(arr , (3,4)))

#flatten / ravel
var = np.resize(arr , (4,3))
print(var)
print(np.ravel(var))