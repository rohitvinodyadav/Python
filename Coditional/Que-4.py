# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = int(input("Select the colour of Banana \n 1. Green \n 2. Yellow \n 3. Brown \n"))

if color == 1:
    print("Unripe")
elif color == 2:
    print("Ripe")
elif color == 3:
    print("Overripe")
else:
    print("Select a valid color")