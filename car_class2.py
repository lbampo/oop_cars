from vehicle_class2 import *

class Car2(Vehicle2):
    def __init__(self, wheels, capacity, colour, make, model, license_plate):
        super().__init__(wheels, capacity, colour)
        self.make = make
        self.model = model
        self.license = license_plate
        self._accidents = 0 # visibility is limited
        self.__miles = 100000 # visibilty and access is restricted



    def make_sound(self):
        return ' ReviNNGGGG MY CArRRR'

    def play_music(self, song):
        return f' play {song} '

    def show_miles(self):
        return self.__miles

    def set_miles(self, miles):
        self.__miles = miles
        return 'miles set to' +  miles

    def show_miles(self):
        return self.__miles


print("Proof of Inheritance")
car_example = Car2(2, 4, 'Blue', 'Volvo', 'XC90', 'XOXO')
print(car_example)
print(car_example.accelerate())



#
# print(Car2(2, 4, 'Blue').accelerate())
#
#
# print("Proof of Polymorphism")
# print(Vehicle2(2, 4, 'Blue').make_sound())
# print(Car2 (2, 4, 'Blue').make_sound())
