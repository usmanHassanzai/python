num = int(input("Enter the number that you want to check wether it is prime or not : "))

#checking the number
if(num == 2):
    print("prime number")

#checking the number in loop
for i in range(2 , num):
    if(num % i == 0):
        print(f"not prime")
        break
else:
    print(f"prime")