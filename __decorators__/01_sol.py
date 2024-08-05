import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"Program ran in {end-start} seconds thats is {func.__name__}")
        return result
    print(wrapper)
    return wrapper

# @timer means it can only go through function(toll booth) of timer function
@timer
def example_function(n):
    time.sleep(n)

example_function(3)
