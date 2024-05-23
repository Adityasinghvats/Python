print("aditya")
print("chai is here")
hello = "hello!"

# >>> file = open('chai.py')
# >>> file.readline()
# 'print("aditya")\n'
# >>> file.readline()
# 'print("chai is here")\n'
# >>> file.readline()
# 'hello = "hello!"'
# >>> file.readline()
# ''
# >>> file = open('chai.py')
# >>> file.__next__()
# 'print("aditya")\n'

# >>> for line in open('chai.py'):
# ...     print(line)
# ...
# print("aditya")

# print("chai is here")

# hello = "hello!"

# >>> while True:
# ...     line=file.readline()
# ...     if not line: break
# ...     print(line,end='')
# ...
# print("chai is here")
# hello = "hello!"
# >>> iter(file) is file
# True


# >>> test = "hitesh"
# >>> if not test:
# ...     print("chai")
# ...
# >>> test = ""
# >>> if not test:
# ...     print("chai")
# ...
# chai

mylist = [1,2,3,4]
it = iter(mylist)
print(it)
# <list_iterator object at 0x000001ED381C9BD0> output
# memory reference for list iterator is always at starting
print(it.__next__())
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
# StopIteration exception is raised after 4 is printed
# meaning list is complete iterated
# iter(mylist) is mylist -> false hain


# dictionary
# >>> d = {'a':1,'b':2}
# >>> d
# {'a': 1, 'b': 2}
# >>> for key in d.keys():
# ...      print(key)     
# ...
# a
# b

# Range is iterable
# >>> range(5)
# range(0, 5)
# >>> R = range(5)
# >>> R
# range(0, 5)
# >>> I = iter(R)
# >>> next(I)
# 0
# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>