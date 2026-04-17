coffee_size = str(input("Enter you size: "))
shot_input = input("Need Extra Shot: ")
shot_espresso = shot_input.capitalize() == "True" 
if coffee_size == "Small" and shot_espresso == True:
    coffee = coffee_size + "Here is your coffee with Extra Shot"
elif coffee_size == "Small" and shot_espresso == False:
    coffee = coffee_size + "Coffee"

elif coffee_size == "Medium" and shot_espresso == True:
    coffee = coffee_size + "Here is your coffee with Extra Shot"
elif coffee_size == "Medium" and shot_espresso == False:
    coffee = coffee_size + " Coffee"
elif coffee_size == "Large" and shot_espresso == True:
    coffee = coffee_size + " Here is your coffee with Extra Shot"
elif coffee_size == "Large" and shot_espresso == False:
    coffee = coffee_size + " Coffee"
print(coffee)


