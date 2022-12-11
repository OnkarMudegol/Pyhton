class Car:
    wheeels = 4
    def __init__(self,brand,milage):
        self.brand = brand
        self.milage = milage
car1 = Car("BMW", "10 km/l")
car2 = Car("G-Wagon", "10 km/l")
print(car1.brand, car1.milage, car1.wheeels,"wheels")
print(car2.brand, car2.milage, car2.wheeels,"wheels")