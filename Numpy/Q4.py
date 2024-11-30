#write a python program using numpy to perform addition, subtraction, multiplication,division ,mod,power and reciprocal of the numbers.
import numpy as np
num1 = 20
num2= 10

add = np.add(num1 , num2)
print(add)

#adding two arrays
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
add_arr = np.add(arr1 , arr2)
print(add_arr)
"""for addition number of dimension must be equal or 1"""

#subtraction of array
subtract_arr = np.subtract(arr2 , arr1)
print(subtract_arr)

#multiplication of two array
mul_arr = np.multiply(arr1 , arr2)
print(mul_arr)

#divison of array
div_arr = np.divide(arr2 , arr1)
print(div_arr)

#mod of a number
numb1 = 10
numb2 = 2
mod = np.mod(numb1 , numb2)
print(mod)

#power of number
pow = np.pow(10 , 2)
print(pow)

#reciprocal of a number
reciprocal = np.reciprocal(1/10)
print(reciprocal)