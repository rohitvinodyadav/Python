# Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter a number between 1 and 10: \n"))
    if 1 <= number <=10:
        print("Thanks")
        break
    else:
        print("Sorry! Enter a valid number")