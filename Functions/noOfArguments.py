#when we dont know the num of arguments
#tuples 
def name(*args):
    print("My name is:",*args)
name("Onkar","Sudhakar","Mudegol")
def name1(*args):
    print("First name is:",args[0])
name1("Onkar","Mudegol")
