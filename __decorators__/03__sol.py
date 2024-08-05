import time
# Cached return value

def cache(func):
    # Empty dixt used for easy access through keys
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            print("Inside wrapper:" , cache_value[args])
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_func(a,b):
    time.sleep(4)
    return a+b

print(long_func(5,3))
print(long_func(5,3))
print(long_func(4,3))
print(long_func(5,3))

    