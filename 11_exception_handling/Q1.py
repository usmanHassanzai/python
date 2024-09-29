#Exception handling concep
#here we have try and except block 
try:
    print(f"division of 4 by 2 is : {4 / 2}")
    print(f"division of 4 by 0 is : {4 / 0}")
    print("Everything divided successfully.")
except ZeroDivisionError:
    print("Do not ask me to divide by 0 please.")
        
print("Done")

