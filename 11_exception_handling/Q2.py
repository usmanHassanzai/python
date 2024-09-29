# Function for division
def div(num1 , num2):
    return (num1 / num2)

# Function for multiplication
def mul(num1 , num2):
    return (num1 * num2)

# Function for addition
def add(num1 , num2):
    return (num1 + num2)

# Function for subtraction
def sub(num1 , num2):
    return (num1 - num2)

# Getting user input
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

operator = input("Enter the operation you want (+, -, *, /): ")

def calculator(operator, num1, num2):
    try:
        if operator == '/':
            return div(num1, num2)
        elif operator == '*':
            return mul(num1, num2)
        elif operator == '+':
            return add(num1, num2)
        elif operator == '-':
            return sub(num1, num2)
        else:
            return "Invalid operator!"
    except ZeroDivisionError:
        return "Do not ask me to divide by zero, please."

# Output the result
print(calculator(operator, num1, num2))
