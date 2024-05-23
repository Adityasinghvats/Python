# >>> tea_types = ("black", "green", "oolong")
# >>> print(tea_types)
# ('black', 'green', 'oolong')
# >>> tea_types[1]
# 'green'
# >>> tea_types[1:]
# ('green', 'oolong')
# All slicing dicing operation are allowed just as a list

# >>> tea_types[0] = "lemon"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment


# >>> more_tea = ("herbal", "earl gray")
# >>> all_tea = tea_types + more_tea
# >>> print(all_tea)
# ('black', 'green', 'oolong', 'herbal', 'earl gray')
# >>> if "green" in all_tea:
# ...     print("yes")
# ...
# yes


# Assining the value of tuple to a tuple with same number of elements
# >>> (Black, Green, Oolong) = tea_types
# >>> Black
# 'black'
# >>> Oolong
# 'oolong'
# >>> type(tea_types)
# <class 'tuple'>


# nested tuple
# >>> tup = ("ADitya",("Hi","hello","how"),10)      
# >>> print(tup)
# ('ADitya', ('Hi', 'hello', 'how'), 10)