import inspect

def foo():
    return 'bar'

print(inspect.isfunction(foo)) # True

print( inspect.isfunction('') ) # False
print( inspect.isfunction(42) ) # False
print( inspect.isfunction([]) ) # False

