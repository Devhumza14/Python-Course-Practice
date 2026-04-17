# Multiplication Table of a number up to 10 but to skip 5th iteration 
number = int(input("Enter the Number "))

for i in range(1, 11):
        if i == 5:
                continue
        print(number, "x" ,i ,"=", number * i)
