# Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

size = int(input("Select the size of the coffee \n 1. Small \n 2.Medium \n 3.Large \n"))
extraShot = int(input("Do you want Extra Shot \n 1. Yes \n 2. No \n"))

if size == 1:
    if extraShot == 1:
        print("One small coffee with extra shot")
    elif extraShot == 2:
        print("One small coffee")
    else:
        print("Select Valid Option")

elif size == 2:
    if extraShot == 1:
        print("One medium coffee with extra shot")
    elif extraShot == 2:
        print("One medium coffee")
    else:
        print("Select Valid Option")

elif size == 3:
    if extraShot == 1:
        print("One large coffee with extra shot")
    elif extraShot == 2:
        print("One large coffee")
    else:
        print("Select Valid Option")

else:
    print("Select valid option")