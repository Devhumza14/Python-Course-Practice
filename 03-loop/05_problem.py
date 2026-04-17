# Find the first non repeated character in the string
str_input = str(input("Enter the String: ")).lower()

for i in str_input:
    if str_input.count(i) == 1:
        print("First Non Repeated character is: ",i)
        break
else:
    print("No unique letter found")
    