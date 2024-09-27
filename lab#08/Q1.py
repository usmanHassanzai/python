number = int(input("Enter the number of which you find the sum of factorial"))

sum_of_factorial = 0

if(number == 0):
    sum_of_factorialfactorial = 1
    
for i in range(1 , number + 1):
    factorial = 1
    for j in range(1 , i + 1):
        factorial = factorial * j
        
    sum_of_factorial = sum_of_factorial + factorial

print(sum_of_factorial)