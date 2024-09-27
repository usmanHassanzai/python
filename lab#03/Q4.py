seconds = int(input("Enter how many seconds you want to convert : "))

hour = int(seconds / 3600)
minutes = int((seconds % 3600) / 60)
second = int((seconds % 3600) % 60)

print(f"{hour} hours, {minutes} minutes, {second} seconds ")