# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday

age = int(input("Enter your age \n"))
day = int(input("Is today Wednesday \n 1.Yes \n 2.No \n"))

if age >= 18:
    if day == 1:
        print("Price is $10")
    else:
        print("Price is $12")
else:
    if day == 1:
        print("Price is $6")
    else:
        print("Price is $8")