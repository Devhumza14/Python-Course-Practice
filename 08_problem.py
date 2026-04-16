# password = input("Enter Your Password: " )

# if len(password) < 6:
#     pass_strengh = "Weak"
# elif len(password) <= 10:
#     pass_strengh = "Medium"
# elif len(password) > 10:
#     pass_strengh = "Strong"
# print("Password strenght is",pass_strengh)
# exit()


password = input("Enter Your Password: " )
pass_strengh = len(password)
if pass_strengh < 6:
    pass_strengh = "Weak"
elif pass_strengh <= 10:
    pass_strengh = "Medium"
elif pass_strengh > 10:
    pass_strengh ="Strong"
print("Password strenght is",pass_strengh)
exit()