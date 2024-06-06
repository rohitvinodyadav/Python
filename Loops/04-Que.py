# Reverse a String
# Problem: Reverse a string using a loop

inputString = input("Enter a string\n")
reverseString = ""

for char in inputString:
    reverseString = char + reverseString

print(reverseString)