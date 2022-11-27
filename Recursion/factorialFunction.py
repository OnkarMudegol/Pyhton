#to make factorial function
def fact(n):
    if n==0:
        return 1

    return n * fact(n-1)

n = int(input("Enter n:"))
num = fact(n)
print(num)