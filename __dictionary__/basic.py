# It does not follow index here we have keys for each element which can be treated as index
# >>> chai_types = {"masala":"spicy","ginger":"zesty", "green":"mild"}
# >>> chai_types
# {'masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}
# >>> chai_types.get("masala")
# 'spicy'
# >>> chai_types["green"] = "fresh"
# >>> chai_types
# {'masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh'}


# In list we get keys in iteration
# >>> for chai in chai_types:
# ...     print(chai)
# ... 
# masala
# ginger
# green

# >>> for chai in chai_types:
# ...      print(chai,chai_types[chai])   
# ...
# masala spicy
# ginger zesty
# green fresh

# >>> for key,value in chai_types.items():
# ...     print(key,value)
# ...
# masala spicy
# ginger zesty
# green fresh

# >>> if "masala" in chai_types:
# ...     print("Masala is present")
# ...
# Masala is present

# >>> print(len(chai_types))
# 3
# >>> chai_types["earl ginger"] = "citrus"
# >>> chai_types
# {'masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh', 'earl ginger': 'citrus'}
# >>> chai_types.pop("green")
# 'fresh'
# >>> chai_types
# {'masala': 'spicy', 'ginger': 'zesty', 'earl ginger': 'citrus'}
# >>> chai_types.popitem()
# ('earl ginger', 'citrus')
# >>> chai_types
# {'masala': 'spicy', 'ginger': 'zesty'}


# >>> tea_shop = {
# ... "chai":{"masala":"spicy","ginger":"zesty"}, "biscuit":{"sweet":"gooday","salty":"monaco"}}
# >>> tea_shop
# {'chai': {'masala': 'spicy', 'ginger': 'zesty'}, 'biscuit': {'sweet': 'gooday', 'salty': 'monaco'}}
# >>> tea_shop["chai"]["ginger"]
# 'zesty'


# first {key:value}
# >>> squared_num = {x:x**2 for x in range(6)}
# >>> squared_num
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# >>> squared_num.clear()
# >>> squared_num
# {}

# >>> keys = ["masala" ,"ginger", "lemon"]
# >>> keys
# ['masala', 'ginger', 'lemon']
# >>> default_value = "delicious"
# >>> new_dict = dict.fromkeys(keys, default_value)
# >>> new_dict
# {'masala': 'delicious', 'ginger': 'delicious', 'lemon': 'delicious'}
# >>> new_dict = dict.fromkeys(keys, default_value)
# >>> new_dict = dict.fromkeys(keys, keys)          
# >>> new_dict
# {'masala': ['masala', 'ginger', 'lemon'], 'ginger': ['masala', 'ginger', 'lemon'],
#  'lemon': ['masala', 'ginger', 'lemon']}