a='hello'
b=42

# type will give a type object
print( type(a) ) # <class 'str'>

# if for some reson I just want the name of the type
# I can use the .__name__ property
print( type(a).__name__ ) # str