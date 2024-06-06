# Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration

number = int(input("Enter the number whose table you want\n"))

for i in range(1,11):
    if i == 5:
        continue
    else:
        print(number, "x", i, "=", number*i)