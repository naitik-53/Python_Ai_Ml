#Take Diameter As Input And Calculate Area Of Circle
import math
diameter = float(input("Enter Diameter Of Circle: "))
radius = diameter / 2
area = math.pi * radius * radius
print("The Area Of Circle Is:", area)   


#Take Radius As Input And Calculate Circumference Of Circle
radius = float(input("Enter Radius Of Circle: "))
circumference = 2 * math.pi * radius
print("The Circumference Of Circle Is:", circumference)

#Take Length And Breadth As Input And Calculate Area Of Rectangle
length = float(input("Enter Length Of Rectangle: "))
breadth = float(input("Enter Breadth Of Rectangle: "))
area_rectangle = length * breadth
print("The Area Of Rectangle Is:", area_rectangle)

#Take Base And Height As Input And Calculate Area Of Triangle
base = float(input("Enter Base Of Triangle: "))
height = float(input("Enter Height Of Triangle: "))
area_triangle = 0.5 * base * height
print("The Area Of Triangle Is:", area_triangle)