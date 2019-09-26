from vehicles_class import *
from car_class import *
from bike_class import *
from car_class2 import *
from vehicle_class2 import *

print("------------ VEHICLE TEST --------")

vehicle_1 = Vehicle(3, 5, 'Green', '1993')

print(f"The vehicle has {vehicle_1.wheels} wheels")

print(vehicle_1.accelerate())


print(vehicle_1.turn())

#---------------------------------------------------------
print("---------- CAR TEST------")

# INPUT VOLUME OF MUSIC #
volume = int(input("What is your volume? "))

# INPUT VALUES INTO CARS ATTRIBUTES (characteristics) #
car_1 = Car(4, 5, 'Red', 1992, 'Mercedes', 'A-Class ', 'L8A 7', False)

# PRINT STATEMENT FOR CAR METHODS (behaviour)
print(f" Wow your car is a  {car_1.capacity} - {car_1.model}")

print(car_1.play_music(volume))

#-------------------------------------------------------------
print("---------- BIKE TEST -----")

bike_1 = Bike(2, 1, 'Black and Yellow', '2 years', 6, "Normal", "No basket")

print(bike_1.year)

print('\n')
#-----------------------------------------------------------------

print("Playing with encapsulation ")
print(car_example.wheels)

car_example._accidents = 100
print(car_example.__miles)

