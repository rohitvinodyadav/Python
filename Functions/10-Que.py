# Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number

def factorialFunction(num):
    if num == 0:
        return 1
    else:
        return num * factorialFunction(num-1)
    
print(factorialFunction(5))