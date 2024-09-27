num_1 = int(input("Enter the value of num_1 : "))
num_2 = int(input("Enter the value of num_2 : "))
operation = input("Enter the operation that you want to perform(*,/,+,-,%) : ")

if(operation == "+" ):
    sum = num_1 + num_2
    print(f"Sum of two numbers are : {sum}")
elif(operation == "-"):
    difference = num_1 - num_2
    print(f"Difference of two numbers are : {difference}")
elif(operation == "*"):
    product = num_1 * num_2
    print(f"Product of two numbers are : {product}")
elif(operation == "/"):
    division = num_1 / num_2
    print(f"Division of two numbers are : {division}")
elif(operation == "%"):
    modulus = num_1 % num_2
    print(f"Modulus of  two numbers are : {modulus}")
else:
    print(f"Invalid operation")