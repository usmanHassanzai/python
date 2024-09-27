seconds = int(input("How many seconds you want to convert : "))
hours = int(seconds / 3600)
minutes = int((seconds % 3600) / 60)
second = int(seconds % 3600 % 60)

print(f"{hours} hours {minutes} minutes and {second} seconds")