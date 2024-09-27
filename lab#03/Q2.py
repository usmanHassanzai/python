number = 321
first_number = int(number / 100)
second_number = int((number % 100) / 10)
third_number = int((number % 100) % 10)

reverse =  int(str(third_number) + str(second_number) + str(first_number))
print(f"reverse of {number} is : {reverse}")
