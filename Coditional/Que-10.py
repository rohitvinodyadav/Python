# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)

petType = int(input("Select you pet type\n1. Dog\n2. Cat\n"))
petAge = int(input("Enter the age of your pet\n"))

if petType == 1:
    if petAge < 2:
        foodType = "Puppy Food"
    else:
        foodType = "Senior Dog Food"

else:
    if petAge < 2:
        foodType = "Kitten Food"
    else:
        foodType = "Senior Cat Food"

print("As your pet is", petAge, "years old. We suggest", foodType)