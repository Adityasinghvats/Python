def myName(name):
    def yourName(name2):
        return name2
    return yourName

f = myName("Aditya")

print(f("Aditi"))