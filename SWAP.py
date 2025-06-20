a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Before (temp):", a, b)
temp = a
a = b
b = temp
print("After (temp):", a, b)

a = int(input("\nEnter a: "))
b = int(input("Enter b: "))
print("Before (no temp):", a, b)
a, b = b, a
print("After (no temp):", a, b)

