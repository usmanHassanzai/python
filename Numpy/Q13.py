import numpy as np 

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)

for i in  arr:
    for j in i:
        print(j) 
print("end")  
 
for i in  np.nditer(arr):
    print(i)
    
    