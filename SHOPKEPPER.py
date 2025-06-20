class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price * item.quantity
    return total
items = [
    Item("Apple", 0.5, 4),
    Item("Banana", 0.3, 6),
    Item("Orange", 0.8, 3)
]
total_cost = calculate_total(items)
print(f"Total cost: ${total_cost:.2f}")
