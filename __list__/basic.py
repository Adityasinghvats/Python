# same slice splice optons are also available here
#  >>> tea_var = ["green" ,"black" ,"oolong"]
# >>> tea_var
# ['green', 'black', 'oolong']
# >>> tea_var_new = tea_var
# >>> tea_var_new
# ['green', 'black', 'oolong']
# >>> tea_var[2] = "white"
# >>> tea_var
# ['green', 'black', 'white']
# >>> tea_var_new
# ['green', 'black', 'white']
# >>> tea_new_var = tea_var.copy()
# >>> tea_var
# ['green', 'black', 'white']
# >>> tea_new_var
# ['green', 'black', 'white']
# >>> tea_var [0] = "blue"
# >>> tea_var
# ['blue', 'black', 'white']
# >>> tea_new_var
# ['green', 'black', 'white']
# >>> tea_new_var.append("yellow")
# >>> tea_new_var
# ['green', 'black', 'white', 'yellow']
# list comprehension
# y = range(10)
# print(y) gts us range(0, 10) excluding 10
# >>> squared_num = [x**2 for x in range(10)]
# >>> print(squared_num)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> cube_num = [x**3 for x in range(5)]
# >>> print(cube_num)
# [0, 1, 8, 27, 64]