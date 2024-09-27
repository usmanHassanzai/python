# Get input from the user
a = int(input("This program will print natural numbers from 1 to 50\nHow many elements are in a row? "))

# Loop to print numbers from 1 to 50
for b in range(1, 51):
    print(b, end="\t")
    if b % a == 0:
        print()  # Move to the next line after printing 'a' numbers
