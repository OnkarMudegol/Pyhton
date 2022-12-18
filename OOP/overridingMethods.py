class Birds:
    def category(self):
        print("This is a bird")
    def fly(self):
        print("Birds can fly")
class Sparrow(Birds):
    def size(sellf):
        print("I am small in Size")
class Crow(Birds):
    pass
class Ostrich(Birds):
    def fly(self):
        print("I cant't fly") #Overriding the method
objBird = Birds()
objSparrow = Sparrow()
objCrow = Crow()
objOstrich = Ostrich()
objBird.category()
objSparrow.category()
objSparrow.size()
objCrow.category()
objOstrich.category()
objBird.fly()
objSparrow.fly()
objSparrow.fly()
objCrow.fly()
objOstrich.fly()