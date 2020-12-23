a=[ ['pow', 2,4], ['div', 16,7], ['sum', 6, 7] ]
b=[];
for params in a:
    what=params[0]
    p1=params[1]
    p2=params[2]
    if(what == 'pow'):
        b.append(pow(p1, p2))
    if(what == 'div'):
        b.append(p1 / p2)
    if(what == 'sum'):
        b.append(p1 + p2)
print(b) # [16, 2.2857142857142856, 13]