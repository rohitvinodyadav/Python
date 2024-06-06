# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n

number = int(input("Enter the number\n"))
evenNumberSum = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        evenNumberSum = evenNumberSum + num

print(evenNumberSum)