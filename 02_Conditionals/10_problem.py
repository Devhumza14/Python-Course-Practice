# Pet food recommendation
pet = input("Enter Pet Specie name ").capitalize()
age = int(input("Enter age of your pet "))

if (pet == "Dog"):
    if age < 2:
        rcdm_food = "Puppy Food"
    else:
        rcdm_food = "Adult Dog Food"

elif (pet == "Cat"):
    if age > 5:
        rcdm_food = "Senior cat food"
    else:
        rcdm_food = "Junior cat food"

else:
        rcdm_food = "Unknown Specie"
print(rcdm_food)


