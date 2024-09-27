number = int(input("Enter the three digit number : "))

def reverse(number):
    first_number = int(number / 100)
    second_number = int((number % 100) / 10)
    third_number = int((number % 100) % 10)
    
    reverse_number = int(str(third_number) + str(second_number) + str(first_number))
    print(f"{number} reverse is : {reverse_number}")
    
reverse(number)