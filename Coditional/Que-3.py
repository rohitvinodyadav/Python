# Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)

score = input("Enter your score \n")
score_in_int = int(score)

if score_in_int > 100 :
    print("Enter a valid score")
    exit()

if score_in_int >= 90 :
    grade = "A"
elif score_in_int >= 80 :
    grade = "B"
elif score_in_int >= 70 :
    grade = "C"
elif score_in_int >= 60 :
    grade = "D"
else :
    grade = "F"

print(grade)