#to take dimensions as user input and calculate area of trapezium
print("A trapezium is a quadrilateral having a set of opposite sides parallel to each other.")
side1 = float(input("Parallel side 1:"))
side2 = float(input("Parallel side 2:"))
height = float(input("Height:"))
area = (side1+side2)*height/2
print("The area of trapezium is:",area)