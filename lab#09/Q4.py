lst = []
odd = []
even = []

for i in range(1 , 11):
    element = int(input("Enter the value of element to store it in list : "))
    lst.append(element)
   
   
count_odd = 0
count_even = 0

#counting even and odd element in list    
for i in lst:
    if(i % 2 == 0):
        count_even += 1
        even.append(i)
        continue
    else:
        count_odd += 1
        odd.append(i)

#display odd and even element 
print(lst)
print(f"Even element are : {count_even}")
print(even)
print(f"Odd elements are : {count_odd}")
print(odd)
        