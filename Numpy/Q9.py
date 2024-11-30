#normalizing rows and columns
import numpy as np
x = np.array([[0 , 3 , 4],
              [1 , 6 , 4]])
#often we wish to normalize value of a row to fall with in a specific range
#divide by maximum

x_norm = np.amax(x , axis = 1)  #if we did not give axis then it will take the maximum value in matrix
#if we take axis then it will print maximum of each row
print(x_norm)

#div = x / x_norm       it will give broadcast error
#print(div)

x_nor = np.reshape(x_norm, (2 , 1))
div = x / x_nor
print(div)

#other method or normilazion

x_normilization = np.linalg.norm(x ,ord=2, axis = 1 , keepdims = True)
print(x_normilization)

normi = x / x_normilization
print(normi)