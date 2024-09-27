    
def table(number):
    for i in range(1 , 11):
        table = number * i
        print(f"{number} X {i} = {table}")
       
while(True):
    number = int(input("Enter a number : "))
    table(number)
    ask_user = input("Do you want to print another number or not? y/n or Y/N : ")
    if(ask_user == 'y' or ask_user == 'Y'):
        continue
    elif(ask_user == 'n' or ask_user == 'N'):
        print(f"Thank you for using our program")
        break 