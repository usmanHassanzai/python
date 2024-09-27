charactor = input("Enter a character: ")
rows = int(input("How many rows (for the top part of the pyramid): "))

# Top part of the pyramid
for h in range(1, rows + 1):
    for j in range(h):
        print(f"{charactor}", end=" ")
    print()  # Move to the next line after each row

# Bottom part of the pyramid (inverted)
for h in range(rows - 1, 0, -1):
    for j in range(h):
        print(f"{charactor}", end=" ")
    print()  # Move to the next line after each row
