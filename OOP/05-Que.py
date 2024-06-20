# Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def fuelType(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand,model)
        self.battery = battery
    
    def fuelType(self):
        return "Electric"
    
myCar = Car("TATA" , "Safari")
myElectricCar = ElectricCar("TESLA", "S1", "84kW")

print(myCar.fuelType())
print(myElectricCar.fuelType())
