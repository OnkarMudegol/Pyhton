#making a division function
a=int(input("a:"))
b=int(input("b:"))
def quoteint(a,b):
    quo=a/b
    return quo
def remainder(a,b):
    remainder=a%b
    return remainder
quoteint(a,b)
remainder(a,b)
print("The quoteint is:{}".format(quoteint(a,b)))
print("The remainder is:{}".format(remainder(a,b)))