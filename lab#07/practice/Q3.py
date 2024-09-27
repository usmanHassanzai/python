number = int(input("Enter the number that you want to calculate the factorial : "))
factorial = 1 # factorial starts from 1
i = 1 #iteration value

while (i <= number):
    factorial = factorial * i
    i = i + 1

#value of factorial is 
print(factorial)