#  List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["banana", "apple", "orange", "apple", "mango"]
uniqueItems = set()

for i in items:
    if i in uniqueItems:
        print("Duplicate Item:", i)
        break
    else:
        uniqueItems.add(i)