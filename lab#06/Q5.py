weight = int(input("Enter the weight of the package in kg :"))
distance = int(input("Enter the distance to ship in miles : "))

if(weight <= 0 or weight > 20):
    print(f"Sorry weight can not be negative, zero or greater than 20 kg")

elif(distance < 10 or distance > 3000):
    print(f"Sorry TCS does not deliver to such distance")

elif(weight > 0 and weight <= 2):
    rate_per_500_mile_shipped = 1.10
    rate_per_mile = rate_per_500_mile_shipped / 500
    charge = rate_per_mile * distance
    print(f"Thank you ")
    print(f"Total Charges : {charge}")

elif(weight > 2 and weight <= 6):
    rate_per_500_mile_shipped = 2.20
    rate_per_mile = rate_per_500_mile_shipped / 500
    charge = rate_per_mile * distance
    print(f"Thank you ")
    print(f"Total Charges : {charge}")
    
elif(weight > 6 and weight <= 10):
    rate_per_500_mile_shipped = 3.70
    rate_per_mile = rate_per_500_mile_shipped / 500
    charge = rate_per_mile * distance
    print(f"Thank you ")
    print(f"Total Charges : {charge}")
    
elif(weight > 10 and weight <= 20):
    rate_per_500_mile_shipped = 4.80
    rate_per_mile = rate_per_500_mile_shipped / 500
    charge = rate_per_mile * distance
    print(f"Thank you ")
    print(f"Total Charges : {charge}")