#!/usr/bin/python3
import disp

# I can create a single display object like this
x=disp.createBasic(5,7)
print(x) # {'x': 5, 'y': 7, 'w': 32, 'h': 32}

# I can create a pool of display objects like this
b=disp.createPool(3, x=50, y=25, create=disp.createEnemy)
obj = b['obj']
print(len(obj)) # 3
print(obj[2])   # {'x': 50, 'y': 25, 'w': 32, 'h': 32, 'hpMax': 100, 'hp': 100, 'attack': 1}
