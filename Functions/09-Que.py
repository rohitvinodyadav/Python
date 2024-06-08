# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit

def evenGenerator(number):
    for num in range(2, number+1, 2):
        yield num
    
for even in evenGenerator(10):
    print(even)