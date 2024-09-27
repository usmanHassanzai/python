for i in range(1, 6):  # Loop to control the number of rows
    for j in range(5, i, -1):  # Print spaces
        print(" ", end="")
    for k in range(0, i):  # Print stars
        print("*", end="")
    print()  # Move to the next line after each row
