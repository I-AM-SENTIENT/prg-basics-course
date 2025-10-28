###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_s = input('a=')
b_s = input('b=')
c_s = input('c=')

a = int(a_s)
b = int(b_s)
c = int(c_s)

volume = a*b*c
surface_area = a*b*2 + b*c*2 + a*c*2

print(f"volume is {volume}")
print(f"surface area is {surface_area}")