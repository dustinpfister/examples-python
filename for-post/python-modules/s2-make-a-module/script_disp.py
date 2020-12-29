#!/usr/bin/python3
import disp

x=disp.createBasic(5,7)
b=disp.createPool(3, x=50, y=25, create=disp.createEnemy)

print(x) # {'x': 5, 'y': 7, 'w': 32, 'h': 32}
print(b['obj'])
