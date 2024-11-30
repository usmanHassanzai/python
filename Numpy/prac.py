import numpy as np

#broadcasting 
#General Rule: Two dimensions are compatible when 1. When they are equal 2.One of them is 1
x0 = np.array([[1],[2]])
x1 = np.array([[1,2,3],[1,2,3]])
print(x0.shape)
print(x1.shape)

x2 = np.array([1,2,3,4])
x3 = np.array([1,2,3])
#print(x2+x3)
#print(x0+x1)

x4 = x3 + 4
print(x4)
