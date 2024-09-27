side_1 = 60
side_2 = 70

#defining function
def triangle(side_1 , side_2):
    side_3 = 180 - (side_1 + side_2)
    return side_3

side3 = triangle(side_1 , side_2) #function call
print(f"The third side of a triangle is : {side3}")