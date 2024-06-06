# Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = int(input("Select the current weather \n 1. Sunny \n 2. Rainy \n 3. Snowy \n"))

if weather == 1:
    activity = "Go for a walk"
elif weather == 2:
    activity = "Read a book"
elif weather == 3:
    activity = "Build a snowman"
else:
    print("Select a valid weather")

print(activity)