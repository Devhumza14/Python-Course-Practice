# sum of even number up to n

num = int(input("ENTER NUMBER: "))
sum_of_even = 0

for i in range(1,num+1):
    if i%2 == 0:
        sum_of_even = sum_of_even + 1

print("Count of even number is", sum_of_even)
