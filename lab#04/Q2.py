num_1 = int(input("Enter the value of num_1 : "))
num_2 = int(input("Enter the value of num_2 : "))
num_3 = int(input("Enter the value of num_3 : "))

if(num_1 > num_2 and num_1 > num_3  ):
    print(f"First number {num_1} is greater than {num_2} and {num_3}")
elif(num_2 > num_1 and num_2 > num_3):
    print(f"Second number {num_2} is greater than {num_1} and {num_3}")
else:
    print(f"Third number {num_3} is greater than {num_1} and {num_2}")