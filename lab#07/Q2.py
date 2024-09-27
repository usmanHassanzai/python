# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get two numbers from the user
start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

# Display all prime numbers between the two numbers
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
