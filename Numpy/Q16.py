#Numpy array function (where , sort ,search_sort , )
#search array
# we use where function that will return the index number of the element present in an array
import numpy as np 

arr = np.array([1,2,3,4,5,6,7,2,8,9])
search = np.where(arr == 2)
print(search)

#search sorted array
#it will give the position/index that where it will be place
sorted_search = np.searchsorted(arr , 5)
print(sorted_search)

#sort array
print(np.sort(arr))