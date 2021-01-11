import inspect
print(inspect.ismodule(inspect)); # True

# this can slo be done with the type built in
# function with an expression like this:
print( type(inspect).__name__ == 'module' ) # True
