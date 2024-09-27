lst = []
for i in range(1,26):
    user = int(input("Enter the element in list between 10 and 100 Please : "))
    if(user < 10 or user > 100):
        print("Number is less than 10 or greater than 100")
        continue
    elif(user in lst):
        print("Number already exist")
        continue
    else:
        lst.append(user)
        
#display the element of list
print(lst)