class A:
    def __init__(self):
        print("This is a init of method A")
    def method1(self):
        print("This is method 1")
# multilevel inheritance
class B(A): #B is inherite form A 
    def method2(self):
        print("This is method 2")
class C(B): #C is the child of B class
    def method3(self):
        print("This is method 3")
# multiple inheritance 
class E():
    def method4(self):
        print("This is methos 4")
class F(A,E):
    def method5(self):
        print("This is methos 4")
Obj = A()
Obj2 = B()
Obj3 = C()
Obj2.method1() #B is the child of A class
Obj3.method1()