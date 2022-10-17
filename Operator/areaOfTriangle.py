#find area of triangle
#Herons Formula
x=input("Enter the first vertice of Triangle")
y=input("Enter the second vertice of Triangle")
z=input("Enter the third vertice of Triangle")
S=int(x)/2+int(y)/2+int(z)/2
area=(S*(S-int(x))*(S-int(y))*(S-int(z)))**0.5
print("The area is",area) 