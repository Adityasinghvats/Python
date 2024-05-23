fruit = input("Enter the fruit to test:").capitalize()

if fruit=="Banana":
    color_fruit = input("Enter color of fruit:").capitalize()
    if color_fruit=="Green":
        print("Unripe")
    elif color_fruit=="Yellow":
        print("Ripe")
    elif color_fruit=="Brown":
        print("Overripe")
else:print("Fruit not recognised")