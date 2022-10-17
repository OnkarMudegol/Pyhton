#take user nput for three sides of triangle
side1 = int(input("Enter first vertice:"))
side2 = int(input("Enter the second vrtice:"))
side3 = int(input("Ennter the third vertice:"))
if side1 + side2 > side3:
    print("The triangle is possible.")
else:print("The triangle is not possible")
