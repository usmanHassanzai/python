def passwd(password):
    print(password)

password = input("Enter a password that must be at least 8 characters long: ")
count_password = len(password)

# Ensure the password is at least 8 characters long
while (count_password < 8):
    print("Password must be at least 8 characters long.")
    password = input("Please enter your password again: ")
    count_password = len(password)

# Check for special character after confirming the password is long enough
if ('%' in password or '!' in password or '*' in password or '^' in password or '&' in password):
    passwd(password)
else:
    print("Password must contain at least one special character.")
    
    # Prompt for a new password with at least one special character
    new_password = input("Enter a password again that must contain at least one special symbol: ")
    
    if (new_password == password):
        print("The new password must be different from the previous one.")
    elif ('%' in new_password or '!' in new_password or '*' in new_password or '^' in new_password or '&' in new_password):
        passwd(new_password)
    else:
        print("Password does not meet the criteria.")
