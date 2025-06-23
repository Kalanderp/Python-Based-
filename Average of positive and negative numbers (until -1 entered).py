positive = []
negative = []
while True:
    num = int(input("Enter number (-1 to stop): "))
    if num == -1:
        break
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
if positive:
    print("Average of positive numbers:", round(sum(positive)/len(positive), 2))
else:
    print("No positive numbers entered.")
if negative:
    print("Average of negative numbers:", round(sum(negative)/len(negative), 2))
else:
    print("No negative numbers entered.")