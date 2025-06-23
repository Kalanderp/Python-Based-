elements = {'a': 3, 'b': 5, 'a': 3, 'c': 2, 'b': 5}
frequency = {}

for key in elements:
    if key in frequency:
        frequency[key] += 1
    else:
        frequency[key] = 1

print("Element frequencies:", frequency)
