# Reverse a String using loop 
str_input = str(input("Enter the String: "))
reversed_str = ""

for i in str_input:
    reversed_str = i + reversed_str
print("Reveresed string is: ",reversed_str)
