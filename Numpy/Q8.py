import numpy as np

x = np.arange(4) # (4,)
print(x)
print(x.shape)

y = np.arange(5)        # (5,)
#sum = x + y
#print(sum)
print(y)
print(y.shape)

yy = y.reshape(5,1) #(5,1)
#print(x.reshape(4,1))
sum = x + yy # (1,4) + (5,1)
print(sum)

add_2_to_x = np.add(x,[2])
print(add_2_to_x)

a = np.array([[0.0 , 0.0 , 0.0],
              [10.0 , 10.0 , 10.0],
              [20.0 , 20.0 , 20.0],
              [30.0 , 30.0 , 30.0]])

b = np.array([1.0 , 2.0 , 3.0 , 4.0])
# it will not add a + b because b shap is (4,) and a shape is (4 , 3)  

bb = b.reshape(4 , 1)
print(bb)
print(bb + a)