class Laptop:                 #defining a class
    
    # def __init__(self):
    #     self.name = "Asus" 
    #     self.processor =  "i9"
    #     self.ssd =  "1TB"
    def __init__(self, name, processor): #init is a constructor, whenever the function starts it works
        self.name = name
        self.processor =  processor
    # def Asus(self):
    #     print("ASUS","i7","1TB")
    # def Acer(self):
    #     print("Acer","i9","4TB")

laptop1 = Laptop("Asus", "i7")            #making objects
laptop2 = Laptop("Acer", "i9")
# laptop1.Asus()
# laptop2.Acer()
# print(laptop1.name)
# print(laptop1.processor)
# print(laptop1.ssd)
print(laptop1.name)
print(laptop2.name)
print(laptop1.processor)
print(laptop2.processor)