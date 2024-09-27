meal_charge = int(input("Enter the meal charge : "))
tax = meal_charge * 0.0475
tip = (meal_charge + tax) * 0.1

total_bill = meal_charge + tax + tip

print(f"Meal cost  : {meal_charge}")
print(f"Tax amount : {tax}")
print(f"Tip amount : {round(tip,2)}")
print(f"Total bill : {total_bill}")