amir = int(input("Enter the age of Amir : "))
ali  = int(input("Enter the age of Ali : "))
haider = int(input("Enter the age of Haider : "))

#creating a function that will take three ages as parameter
def calculate_eldest_one(amir , ali , haider):
    if((amir > ali) and (amir > haider)):
        print(f"Amir is elder than Ali and Haider ")
    elif((ali > amir) and (ali > haider)):
        print(f"Ali is elder than Amir and Haider")
    else:
        print(f"Haider is  elder than Ali and Amir")
    
#funtion call
calculate_eldest_one(amir , ali , haider)
