import math
def area_stats(radius):
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    return round(area,2),round(circumference,2)

radius = int(input("Enter the radius of circle:"))

area , circumference = area_stats(radius)

print("area is:",area,"\ncircumference is:",circumference)

