def div(n=1, d=1):
    try:
        return n / d
    except ZeroDivisionError:
        return 0.0
    except TypeError:
        return 0.0
    
print( div() )             # 1.0
print( div(5, 0) )         # 0.0
print( div('foo', None) )  # 0.0
