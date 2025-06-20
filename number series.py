n = 10
print("Even series:", [i for i in range(2, n+1, 2)])
print("\nNumber Pattern:")
for i in range(1, 6):
    print(' '.join(str(j) for j in range(1, i + 1)))
print("\nPyramid Pattern:")
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)
