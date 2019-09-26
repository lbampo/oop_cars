from vehicles_class import *

class Car(Vehicle):


    def __init__(self, wheels, capacity, colour, year, brand, model, license_plate, airbag ):
        super().__init__(wheels, capacity, colour, year)
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.airbag = airbag


    def play_music(self, volume):
        if volume > 20:
            return 'NAAAAAAA NAAAA NAAA NANANANA NANANANA HEY JUDE'

        else:
            return 'naaaa naaa naaa nananana nananana hey Jude'

    def horn(self):
        return 'BEEEEEEEEEEEEEEEEEEEEP'

    def lock_it(self):
        return 'tik tik'

    def windshield_clean(self):
        return 'sheaakkkk sheakkkk'

    def door_close(self):
        return ' SLAM '

