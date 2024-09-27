lst = []
count = 0
for i in range(0 , 10):
    number = int(input("Enter the value value : "))
    lst.append(number)
    count += 1
print(lst)

# To find the minimum value in the list
minimum_number = min(lst)
print(f"Minimum : {minimum_number}")

# To find the maximum value in the list
maximum_number = max(lst)
print(f"Maximum : {maximum_number}")

# To find the sum of list
total_sum = sum(lst)
print(f"sum : {total_sum}")

# To find the average of the list
list_average = sum / count
print(f"average : {list_average}")

#To find the last element of the list
last_element = lst[-1]
print(f"last element : {last_element}")

#To find the value at index 2
value_at_2 = lst[2]
print(f"Value at index 2 : {value_at_2}")

#Reverse of the list
lst.reverse()   #first we call reverse function
print(f"Reverse : {lst}")

# count even and odd element in list
odd = 0
odd_sum = 0
even = 0 
for i in range(0 , 10):
    if (lst[i] % 2 == 0):
        even += 1
        continue
    else:
        odd_sum = odd_sum + lst[i]
        odd += 1
print(f"odd : {odd}")
print(f"even : {even}")

# print sum of odd indices element
print(f"odd sum : {odd_sum}") 

#count the list
a = lst.count(5)
print(a)