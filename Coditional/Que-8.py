# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password \n")
passwordLength = len(password)

if passwordLength < 6:
    strength = "Weak"
elif passwordLength < 11:
    strength = "Medium"
else:
    strength = "Strong"

print("Your password include", passwordLength ,"character. So your password strength is", strength)