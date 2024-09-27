score = int(input("Enter your score/percentage please : "))
if(score >= 90):
    print(f"Your grade is : A+")
    print(f"super Excelent")
elif(score >= 80 and score < 90):
    print(f"Your grade is : A")
    print("Excelent")
elif(score >= 70 and score < 80):
    print("Your grade is : B")
    print("Good")
elif(score >= 60 and score < 70):
    print("Your grade is : C")
    print(f"Adequate")
elif(score >= 50 and score < 60):
    print("Your grade is : D")
    print("Pass")
else:
    print(f"Your grade is : F")
