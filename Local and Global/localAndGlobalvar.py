#intro to local and global variable
#this is a global variable
a=5
#this is a local variable
def example():
    a=10
    print(a)
example()
print(a)
#to edit a global variable using def
def example():
    global a
    a = 10
    print(a)
example()