# yield -> pause the function keeps stage of variable in memory
# so that it can resume from same point next time it is called
# In Python, the yield keyword is used within a function to turn it into a generator.
# A generator is a special type of iterator that generates values on the fly and
# can be iterated over like a list or array. 
# Unlike a regular function that returns a value and terminates, a generator function 
# returns an iterator object with a sequence of values, allowing the function to
# yield multiple values over time.


def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i 

for num in even_generator(10):
    print(num)