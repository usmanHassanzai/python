classes_arrange = int(input("Enter the total number of classes that instructor arrange : "))
classes_attend = int(input("Enter the total number of classes that student attend : "))

def calculate_attendance(classes_arrange , classes_attend) :
    attendance = (classes_attend / classes_arrange) * 100
    
    #condition apply to check wether he is eligible to sit in exam or not
    if(attendance >= 80):
        print(f"your attendance is : {round(attendance,2)}%")
        print(f"You are allowed to appear in exam")
    else:
        print(f"your attendance is : {round(attendance,2)}%")
        print(f"you are not allowed in exam")
        
#function call
calculate_attendance(classes_arrange , classes_attend)