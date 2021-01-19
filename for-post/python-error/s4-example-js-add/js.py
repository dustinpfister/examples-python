def jsAdd(a=0, b=0):
    try:
        # try just adding first
        return a + b
    except TypeError:
        # TypeError? try converting
        try:
            if type(a).__name__ == 'str':
                a=int(a)
            if type(b).__name__ == 'str':
                b=int(b)
            return a + b
        except ValueError:
            # ValueError? then just convert bolth
            # values to strings and concat
            return str(a) + str(b)

print( jsAdd(1, 2) )      # 3
print( jsAdd(5, 7) )      # 12
print( jsAdd('foo', 800) )  # 'foo800'
