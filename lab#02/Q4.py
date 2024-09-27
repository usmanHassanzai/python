seconds = 86000
minutes = seconds / 60
hours = seconds / 3600
days = seconds / 24 / 3600

print(f"{seconds} seconds have {round(minutes , 2)} minutes ")
print(f"{seconds} seconds have {round(hours , 2)} hours")
print(f"{seconds} seconds have {round(days , 2)} days")