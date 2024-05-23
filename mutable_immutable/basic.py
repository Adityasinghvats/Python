# every data type is an object in python
# when we change the value of a immutable type the reference get shifted to newly
# created block of username
# the value store in previous username box is not changed at all
# which makes it immutable
# automatic gaabage collector will delete the previous created box
# it is very diffeent form constsnts and variables


# >>> username ="Hitesh"  
# >>> username
# 'Hitesh'
# >>> username = "Aditya"
# >>>
# >>> username
# 'Aditya'
# >>> x = 10
# >>> y = x
# >>> x
# 10
# >>> y
# 10
# >>> x = 15
# >>> y
# 10
# >>>