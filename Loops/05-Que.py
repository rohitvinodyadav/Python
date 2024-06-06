# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

testString = input("Enter a string:\n ")

for char in testString:
    if testString.count(char) == 1:
        print(char, "is first non-repeated character")
        break