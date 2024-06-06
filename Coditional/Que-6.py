# Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("Enter the distance \n"))

if distance < 3:
    modeOfTransportation = "Walk"
elif distance <= 15:
    modeOfTransportation = "Bike"
else:
    modeOfTransportation = "Car"

print("As the distance is", distance , "Km.,You should go by", modeOfTransportation)