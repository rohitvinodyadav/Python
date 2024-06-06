# Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
postiveNumberCounter = 0

for num in numbers:
    if num > 0:
        postiveNumberCounter += 1

print("Total number of positive numbers are", postiveNumberCounter)