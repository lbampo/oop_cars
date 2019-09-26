from vehicles_class import *

class Bike(Vehicle):

    def __init__(self, wheels, capacity, colour, year, gear, handle_bar_type, basket_size):
        super().__init__(wheels, capacity, colour, year)
        self.gear = gear
        self.handle_bar_type = handle_bar_type
        self.basket_size = basket_size

    def peddle(self):
        return 'peddddlinggg.. peddddling'

    def wheely(self):
        return 'Wheeeeeelying'

    def chain_it(self):
        return 'cling cling cling... lock'





