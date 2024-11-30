#BROADCASTING CONCEPT
"""General Rule
                Two dimensions are compatible when
                1)They are equal
                2)One of them is 1"""
import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3])
#print(arr1 + arr2)   #broadcasting error

"""To avoid from broadcasting error first we check the array and then set it to avoid from broad cast 
1.if the dimension is 1 X 3 or 3 X 1 it mean if there is any  1 occur in any dimension then it is avoid from broadcasting
2.same number of dimension is also avoid from broadcast
3.we can reshape the array to avoid broadcasting"""

arr3 = np.reshape(arr2,(3,1))
print("shape of arr1 : ",arr1.shape)
print("shape of arr2 : ",arr2.shape)
print("shape of arr3 : ",arr3.shape)
print(arr3 + arr1)
print((arr3 + arr1).shape)