#  Factorial of a number using while loop
number = int(input("Enter your Number: "))
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1
print("Factorial is: ",factorial)
