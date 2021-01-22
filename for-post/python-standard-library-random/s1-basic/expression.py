import random

x_min = 50
x_max = 100
y_min = 225
y_max = 250

x = x_min + ( x_max - x_min ) * random.random()
y = y_min + ( y_max - y_min ) * random.random()

print(x, y)