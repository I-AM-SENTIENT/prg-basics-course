def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area


a = float(input("Enter side a of the triangle: "))
b = float(input("Enter side b of the triangle: "))
c = float(input("Enter side c of the triangle: "))
print('The area of ​​a triangle with sides', a, b, c, 'is', triangle_area(a, b, c))