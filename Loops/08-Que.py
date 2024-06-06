# Prime Number Checker
# Problem: Check if a number is prime

number = int(input("Enter the number\n"))
count = 0

if number > 1:
    for num in range(2, number+1):
        if number % num == 0:
            count = count + 1

if count == 1:
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")