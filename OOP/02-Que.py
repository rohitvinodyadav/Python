# Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def dispalyFullName(self):
        return f"{self.brand} {self.model}"
    
myCar = Car("TATA", "Safari")
print(myCar.dispalyFullName())