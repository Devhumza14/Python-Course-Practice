fruit = input("Enter Fruit: eg Banana: ")
color = input("Enter the Color eg: Green or Yellow: ")
if fruit == "Banana":
    if color == "Green":
        print("Unripe not right for eating")
    elif color == "Yellow":
        print("Ripe perfect you can eat it")
    else:
        exit()
