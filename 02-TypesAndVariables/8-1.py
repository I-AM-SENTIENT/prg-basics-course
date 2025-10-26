import math


radius = float(input('Enter the radius of the circle: '))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
circumference = round(circumference,2)
area = round(area,2)
print(f'The circumference is {circumference} and the area is {area}.')