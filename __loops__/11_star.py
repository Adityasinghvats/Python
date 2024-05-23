height = int(input("Enter the height of pattern:"))

for i in range(1, height+1):
    print("* " * i)

while height>0:
    print("* " * height)
    height -= 1
