#  >>> chai = "Lemon chai"
# >>> chai
# 'Lemon chai'
# >>> chai = "Masala Chai"
# >>> print(chai)
# Masala Chai
# >>> print(chai[0])
# M
# >>> slice_chai = chai[0:6]
# >>> print(slice_chai)
# Masala
# >>> num_list = "0123456789"
# >>> num_list[:]
# '0123456789'
# >>> num_list[0:6]
# '012345'
# >>> num_list[-1:0]
# ''
# >>> num_list[-1:-4]
# ''
# >>> num_list[3:]
# '3456789'
# >>> num_list[:5]
# '01234'
# >>> num_list[0:8:3]
# '036'
# >>> num_list[-1:-6]
# ''
# >>> num_list[-1:5]
# ''
# >>> num_list[0:-4]
# '012345'
# >>> chai
# 'Masala Chai'
# >>> print

# <built-in function print>
# >>> print(chai.lower())
# masala chai
# >>> print(chai.upper())
# MASALA CHAI
# >>> chai
# 'Masala Chai'

# >>> chai = "    Masala Chai     "
# >>> chai
# '\tMasala Chai\t'
# >>> print(chai.strip())
# Masala Chai

# >>> chai = "Lemon Chai"
# >>> print(chai.replace("Lemon", "ginger"))
# ginger Chai

# >>> chai = "Lemon , Ginger, Masala, Mint"
# >>> print(chai.split(", "))
# ['Lemon ,Ginger ,Masala', 'Mint']
# >>> chai = "Masala Chai"
# >>> print(chai.find("Chai"))
# 7
# >>> print(chai.find("chai"))
# -1 When not found gives iT
# >>> chai = "chai chai chai"
# >>> print(chai.count("chai"))
# 3
# >>> chai_type = "masala"
# >>> quantity = 2
# >>> order = "I ordered {} cups of {} chai"
# >>> order
# 'I ordered {} cups of {} chai'
# >>> print(order.format(quantity, chai_type))
# I ordered 2 cups of masala chai
# >>> chai_variety = ["Lemon","Masala","Ginger"]
# >>> print(" , ".join(chai_variety))   
# Lemon , Masala , Ginger
# >>> chai = "he said, \"Masala Chai\" is awesome!" 
# >>> chai
# 'he said, "Masala Chai" is awesome!'
# >>> chai = r"Masala\nChai"
# >>> chai r means raw string
# 'Masala\\nChai'
# >>> chai = "Masala Chai"
# >>> print("Masala" in chai)
# True