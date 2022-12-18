# Make 2 car class and 1 bus class
# In car class make a seating capacity 4 and override in bus
class Vehicles:
    def seatingCapacity(self):
        print("The seating capacity is 4")
class Car1(Vehicles):
    pass
class Car2(Vehicles):
    pass
class Bus(Vehicles):
    def seatingCapacity(self):
        print("The seating capacity is 25")
objCar1 = Car1()
objCar2 = Car2()
objBus = Bus()
objCar1.seatingCapacity()
objCar2.seatingCapacity()
objBus.seatingCapacity()