from abstract_class import *
class Bike(Vehicle):
    def __init__(self,no_of_tyres,color_of_bike):
        super().__init__(no_of_tyres)
        self.color_of_bike=color_of_bike
    def start(self):
        print("start by kick")
    def display(self):
        print(f"I have bike with {self.no_of_tyres} tyres and {self.color_of_bike} color")
class Scooty(Vehicle):
    def start(self):
        print("Start by self")
class Car(Vehicle):
    def start(self):
        print("start by key")
    
