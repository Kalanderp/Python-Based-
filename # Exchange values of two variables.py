# Exchange values of two variables
a, b = 5, 10
a, b = b, a
print("Swapped: a =", a, ", b =", b)

# Circulate values of three variables
x, y, z = 1, 2, 3
x, y, z = z, x, y
print("Circulated: x =", x, ", y =", y, ", z =", z)

# Distance between two points
from math import sqrt
x1, y1, x2, y2 = 0, 0, 3, 4
dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", dist)
