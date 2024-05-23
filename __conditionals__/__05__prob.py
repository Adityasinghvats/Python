order_size = input("Enter you cup size:").capitalize()
# extra_shot = input("Enter true or false:").capitalize()
extra_shot = False
if extra_shot:
    coffee = order_size+" coffee with extra shot"
else:coffee = order_size +" coffee"

print(coffee)