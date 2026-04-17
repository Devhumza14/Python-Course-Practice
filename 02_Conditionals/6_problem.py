distance = int(input("Enter the Distance: "))
if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
elif distance > 15:
    transport = "Car"

print(transport)
