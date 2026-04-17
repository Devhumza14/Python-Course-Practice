marks = int(input("Enter you marks: "))
if marks > 100:
    print("Wrong Entry Enter Correct Marks")
    exit()
elif marks >= 90:
    print('A')
elif marks >= 80:
    print('B')
elif marks >= 70:
    print('C')
elif marks >= 60:
    print('D')
else:
    print('F')
