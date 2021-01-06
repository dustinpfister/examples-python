import os

print(os.name) # posix, nt, or java

# the uname method can be used to get a
# better idea of the kind of system that is being used
# with things like kernal name, kernal version, and
# system arch.
uname=os.uname()
l=list(uname)
print( l[0] ) # Linux
print( l[2] ) # 5.4.79-v7+
print( l[4] ) # armv7l
