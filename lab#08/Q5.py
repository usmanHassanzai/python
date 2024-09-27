charactor = input("Enter a charactor : ")
rows = int(input("How many rows : "))

for i in range(1 , rows+1):
    for j in range(rows , i-1 , -1):
        print(f"{charactor}", end=" ")
    print()