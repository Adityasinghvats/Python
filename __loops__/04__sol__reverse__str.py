input_str = "Pyhton"
reversed_str = ""
for char in input_str:
    # It gives reversed string
    reversed_str = char+reversed_str
    # It gives real one only
    # reversed_str = reversed_str + char 
print(reversed_str)