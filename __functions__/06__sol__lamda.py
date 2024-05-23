# when we need to use function onlyr once or twice 
# we use lambda functions
number = int(input("Enter a number:"))

# lamda (parameter): function work
cube = lambda num: num**3
print("Cube of ",number,"is",cube(number))