# write a function that takes the length and width of a rectangle and returns the area
def area_rect(length, breadth):
    area=length*breadth
    return area
print("--------------------------Area of Rectangle---------------------------------")
l=int(input("enter the length: "))
b=int(input("enter the breadth: "))
print("area of rectangle is : ", area_rect(l,b))

# write another function that finds the area of a cube
# bonus challenge: use your first function inside this function!
def area_cube(side):
    area=6*area_rect(side,side)
    return area
print("--------------------------Area of Cube--------------------------------------")
a=int(input("enter the side length: "))
print("area of cube is : ", area_cube(a))

# write a function that finds the area of a sphere
# hint: you can get `pi` by importing math (google it!)
import math
def area_sphere(radius):
    area=4*math.pi*area_rect(radius,radius)
    return area
print("--------------------------Area of Sphere--------------------------------------")
r=int(input("enter the radius: "))
print("area of sphere is : ", area_sphere(r))