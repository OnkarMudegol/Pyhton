#to make a function to multiply two numbers
a = int(input("a:"))
b = int(input("b:"))
def multiplication(a,b):
    product=a*b
    return product
multiplication(a,b)
print("The product is:{}".format(multiplication(a,b)))