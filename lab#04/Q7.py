per_unit_price = 5
previous_unit = 150
current_unit = 250 
current_month_unit_consumed = current_unit - previous_unit

current_month_bill = per_unit_price * current_month_unit_consumed

print(f"Unit consumed in current month : {current_month_unit_consumed}")
print(f"The current month electricity bill is : {current_month_bill}")
