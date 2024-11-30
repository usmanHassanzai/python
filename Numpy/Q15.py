#concatinate array
#we can merge two array into single array
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
join_array = np.concatenate((arr1 , arr2))
print(join_array)

#split array
#split array breaks one array into multiple
split_array = np.array_split(arr1 , 3)
print(split_array)