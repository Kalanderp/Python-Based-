a, b = 5, 10
temp = a
a = b
b = temp
print("With temp:", a, b)
a, b = 5, 10
a, b = b, a
print("Without temp:", a, b)