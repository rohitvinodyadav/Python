# Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter a number\n"))
num = number
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print("Factorial of", num ,"is", factorial)