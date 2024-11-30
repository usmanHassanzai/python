import numpy as np

# Create an array
array = np.array([1, 2, 3, 4, 5])

# Add 5 to each element using a loop
result = np.empty_like(array)  # Create an empty array of the same shape
for i in range(len(array)):
    result[i] = array[i] + 5

print("Result using loop:", result)

#using vectorization

# Add 5 to each element using vectorized operation
vecrtoriaztion_result = array + 5

print("Result using vectorization:", vecrtoriaztion_result)

#make an array which has element from zero to 1000
arrs = np.arange(1000)
print(arrs)
sum = sum(arrs)
print(sum)