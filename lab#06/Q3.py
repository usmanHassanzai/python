burger = 500
extra  = 200

while(True):
    customer = input("Do you want a burger? Y/N : ")
    if(customer == 'y' or customer == 'Y'):
        print(f"Burger added")
        
        while (True):
            ask_customer = input("Do you want a fries and drink as addon? just for 200 Rs Y/N : ")
            if(ask_customer == 'y' or ask_customer == 'Y'):
                bill = burger + extra
                print(f"fries and drink added")
                print(f"Your total bill is : {bill}")
                break
            elif(ask_customer == 'n' or ask_customer == 'N'):
                bill = burger
                print(f"Your choice! Thank you ")
                print(f"Your total bill is : {bill}")
                break
            else:
                print(f"Invalid input.")
                print(f"Please try again.")
        break 
           
    elif(customer == 'n' or customer == 'N'):
        print(f"No problem. see you next time.")
        break
    else:
        print(f"Invalid input.")
        print(f"Please try again.")