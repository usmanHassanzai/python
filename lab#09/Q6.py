lst = []

for i in range (1 , 16):
    number = int(input("Enter the value of element that you want to store in list : "))
    lst.append(number)
count_distinct = len(set(lst))   
v = list(set(lst)) # To write common element at once in list we use set and we have to store it any variable.list is use to convert it into list
print(f"Distinct elements are : {count_distinct}")
print(v)
