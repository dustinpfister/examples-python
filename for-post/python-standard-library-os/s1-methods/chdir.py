import os

os.chdir('/home') 
print(os.getcwd()) # '/home'

os.chdir('..')
print(os.getcwd()) # '/'