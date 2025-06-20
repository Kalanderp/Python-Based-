from math import pi
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def largest(lst):
    return max(lst)

def area(shape, *args):
    if shape == 'circle': return pi * args[0]**2
    if shape == 'rectangle': return args[0] * args[1]
    if shape == 'square': return args[0] ** 2
    return "Unknown shape"

print("Factorial(5):", factorial(5))
print("Largest:", largest([3, 9, 2, 7]))
print("Area of circle (r=3):", area('circle', 3))
print("Area of rectangle (4x5):", area('rectangle', 4, 5))
print("Area of square (side=4):", area('square', 4))
