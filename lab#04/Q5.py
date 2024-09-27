side_1 = int(input("Enter the value of side_1 : "))
side_2 = int(input("Enter the value of side_2 : "))
side_3 = int(input("Enter the value of side_3 : "))

if(side_1 == side_2 and side_1 == side_3):
    print(f"All sides are equal")
    print(f"Equilateral triangle")
elif(side_1 != side_2 and side_1 != side_3 and side_2 != side_3):
    print(f"All sides are unequal")
    print(f"Scalene triangle")
elif((side_1 == side_2 and side_1 != side_3) or (side_2 == side_3 and side_2 != side_1) or (side_3 == side_1 and side_3 != side_2)):
    print(f"Two sides are equal")
    print(f"Isocelles triangle")