from vehicle_class2 import *

class Car2(Vehicle2):
    def __init__(self, wheels, capacity, colour, make, model, license_plate):
        super.__init__(wheels, capacity, colour)
        self.make = make
        self.model = model
        self.license = license_plate



    def make_sound(self):
        return ' ReviNNGGGG MY CArRRR'

    def play_music(self, song):
        return f' play {song} '

print("Proof of Inheritance")
print(Car2(2, 4, 'Blue'))

print(Car2(2, 4, 'Blue').accelerate())


print("Proof of Polymorphism")
print(Vehicle2(2, 4, 'Blue').make_sound())
print(Car2 (2, 4, 'Blue').make_sound())
