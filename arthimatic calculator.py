def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Error: Division by zero"
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == '+':
    print("Result:", add(x, y))
elif op == '-':
    print("Result:", sub(x, y))
elif op == '*':
    print("Result:", mul(x, y))
elif op == '/':
    print("Result:", div(x, y))
else:
    print("Invalid operator")
