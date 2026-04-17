year = int(input("Enter your year: "))
if (year % 400 == 0 ) or (year % 4 == 0 and year/100 != 0):
    chk_leap_year = "Leap Year"
else:
    chk_leap_year = "Not a Leap year"
print(chk_leap_year)
 